from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^webdj/', include('webdj.urls')),
    (r'^$', include('webdj.urls')),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
)

'''if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
'''
