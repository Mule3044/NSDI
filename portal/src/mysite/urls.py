from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^home/', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^join/', 'blog.views.join', name='join'),
     url(r'^layers/', 'blog.views.layer', name='layer'),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'blog.views.index')
)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                   documnt_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                   documnt_root=settings.MEDIA_ROOT)