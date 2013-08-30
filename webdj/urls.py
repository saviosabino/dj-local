from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView
from webdj.models import Local

urlpatterns = patterns('webdj.views',
    (r'^$', 'index'),
    (r'^list/$', 'list'),
    (r'^(?P<web_id>\d+)/$', 'detail'),
    (r'^(?P<web_id>\d+)/change/$', 'change'),
    (r'^add/$', 'add'),
#    (r'^pathin/$', 'pathin'),
    
)

#urlpatterns += patterns('',
#    (r'^$', ListView.as_view(
#        queryset = Local.objects.order_by('name')[:5],
#        context_object_name = 'latest_locals',
#        template_name = 'webdj/index.html')),
#    (r'^(?P<pk>\d+)/$', DetailView.as_view(
#        model = Local, template_name = 'webdj/detail.html')),
#)

