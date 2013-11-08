from django.conf.urls import patterns#, include, url
from django.views.generic import TemplateView#, DetailView, ListView
#from webdj.models import Local

urlpatterns = patterns('core.views',
    (r'^$', 'index'),
    (r'^list/$', 'list'),
    (r'^(?P<ob_id>\d+)/$', 'detail'),
    (r'^(?P<ob_id>\d+)/change/$', 'change'),
    (r'^add/$', 'add'),
    (r'^search/$', 'search'),
    (r'^jumbo/$', TemplateView.as_view(template_name='jumbotron-narrow.html')),
)

#urlpatterns += patterns('',
#    (r'^$', ListView.as_view(
#        queryset = Local.objects.order_by('name')[:5],
#        context_object_name = 'latest_locals',
#        template_name = 'webdj/index.html')),
#    (r'^(?P<pk>\d+)/$', DetailView.as_view(
#        model = Local, template_name = 'webdj/detail.html')),
#)

