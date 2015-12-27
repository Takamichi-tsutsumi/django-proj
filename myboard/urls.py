from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
        '',
        url('', include('django_socketio.urls')),
        url('', include('websock.urls')),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^cms/', include('cms.urls', namespace='cms')),
        url(r'^simpleboard/', include('simpleboard.urls', namespace='simpleboard')),
)
