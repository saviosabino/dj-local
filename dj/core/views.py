from django.contrib.auth.decorators import login_required
from dj.core import models, forms
from django.shortcuts import render_to_response, get_object_or_404
from django.http import  HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

@csrf_exempt
def search(request):
    data = models.Local.objects.filter(name__contains = request.POST['q'])
    fields = ('name','coordinates','address')
    response_data = serializers.serialize('json', data, fields=fields)
    return HttpResponse(response_data, mimetype='application/json')

def index(request):
    return render_to_response('core/index.html',)

@login_required
def list(request):
    latest_locals = models.Local.objects.all().\
        filter(user=request.user).order_by('name')[:5]
    return render_to_response('core/list.html', {'latest_locals': latest_locals,})

def detail(request, ob_id):
    if request.method == 'POST':
        #comment post
        data = request.POST.dict()
        datenow = datetime.datetime.now()
        data.update({'local': ob_id, 'date': datenow})
        frm = forms.CommentForm(data)
        if frm.is_valid():
            frm.save()
            return HttpResponseRedirect(
                reverse('dj.core.views.detail',args=[ob_id]))
    else:
        frm = forms.CommentForm()
        local = get_object_or_404(models.Local, pk=ob_id)
        return render_to_response(
            'core/detail.html', {'local': local, 'frm': frm}, 
            context_instance = RequestContext(request))

@login_required
def add(request):
    if request.method == 'POST':
        form = forms.LocalForm(request.POST)
        form.coordinates = 0
        if form.is_valid():
            local = form.save(commit=False)
            local.user = request.user
            local.save()
            return HttpResponseRedirect('/list/')
    else:
        form = forms.LocalForm()
        return render_to_response('core/add.html', {'form': form},
            context_instance=RequestContext(request))

@login_required
def change(request,ob_id):
    local = get_object_or_404(models.Local, pk=ob_id)
    if request.method == 'POST':
        form = forms.LocalForm(request.POST, instance=local)
        form.coordinates = 0
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('dj.core.views.detail', args=(ob_id,)))
    else:
        form = forms.LocalForm(instance=local)
        return render_to_response('core/change.html', {'form': form, 'ob_id': ob_id},
            context_instance = RequestContext(request))


