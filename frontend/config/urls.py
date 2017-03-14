from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import views as main_views

from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_views.show_homepage),
    url(r'^api/', main_views.fetch_api_response)
)
