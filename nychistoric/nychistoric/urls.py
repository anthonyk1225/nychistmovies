from django.conf.urls import include, url,patterns
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nychistoric.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^nycfilms/', include('locations.urls')),
)
