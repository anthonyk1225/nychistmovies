from django.conf.urls import include, url,patterns
from django.contrib import admin
from locations.views import IndexView
import locations.views as view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nychistoric.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^',IndexView.as_view(),name='get'),
)
