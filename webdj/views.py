from django.contrib.auth.decorators import login_required

from webdj import models, forms
#from dj.webdj import forms
from django.shortcuts import render_to_response, get_object_or_404
from django.http import  HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
import datetime
import calendar
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

@csrf_exempt
def search(request):
    data = models.Local.objects.filter(name__contains = request.POST['q'])
    #data = list(data.values('id', 'name', 'cord', 'addr'))
    fields = ('name','cord','addr')
    response_data = serializers.serialize('json', data, fields=fields)
    return HttpResponse(response_data, mimetype='application/json')

def index(request):
    return render_to_response('index.html',{'ok':'ok'})

def calSample(request):
    cal = calendar.HTMLCalendar()
    return HttpResponse(cal.formatyear(2012))

#@login_required
def list(request):
    latest_locals = models.Local.objects.all().\
        filter(user=request.user).order_by('name')[:5]
    return render_to_response('list.html', {'latest_locals': latest_locals,})

def detail(request, web_id):
    if request.method == 'POST':
        frm = forms.CommentForm(request.POST)
        if frm.is_valid():
            comment = frm.save(commit=False)
            comment.local_id = web_id
            comment.date = datetime.datetime.now()
            comment.save()
            return HttpResponseRedirect(
                reverse('webdj.views.detail',args=(web_id,)))
    else:
        frm = forms.CommentForm()
    local = get_object_or_404(models.Local, pk=web_id)
    
    return render_to_response(
        'detail.html', {'local': local, 'frm': frm}, 
        context_instance = RequestContext(request))

@login_required
def add(request):
    if request.method != 'POST':
        form = forms.LocalForm()
    else:
        form = forms.LocalForm(request.POST)
        if form.is_valid():
            local = form.save(commit=False)
            local.user = request.user
            local.save()
            return HttpResponseRedirect('/webdj/')
    return render_to_response('add.html', {'form': form},
        context_instance=RequestContext(request))

@login_required
def change(request,web_id):
    local = get_object_or_404(models.Local, pk=web_id)
    if request.method == 'POST':
        form = forms.LocalForm(request.POST, instance=local)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('webdj.views.detail', args=(web_id,)))
    else:
        form = forms.LocalForm(instance=local)
    return render_to_response('change.html', {'form': form, 'web_id': web_id},
        context_instance = RequestContext(request))


