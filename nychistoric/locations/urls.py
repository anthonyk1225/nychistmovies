from django.conf.urls import include, url
from django.contrib import admin
import locations.views as view


urlpatterns = [
    # Examples:
    # url(r'^$', 'nychistoric.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', view.IndexView.as_view(),name='index'),
]