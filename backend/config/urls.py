from django.conf.urls import patterns, include, url
from django.contrib import admin
from people import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'(?P<ID>\d+)/$', views.detail, name='detail'),
    url(r'cars/$', views.cars_by_make, name='cars'),
)
