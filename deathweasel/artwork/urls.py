from django.conf.urls import patterns, include, url
from artwork import views
from artwork.models import ArtworkModel

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('artwork.views',
    url(r'^$', views.ArtListView.as_view(model=views.ArtworkModel),\
            name="top-artwork-page"), 
    url(r'^(?P<pk>\d+)/$',\
            views.ArtModelView.as_view(model=views.ArtworkModel)), 
    url(r'modify/(?P<pk>\d+)/$', views.modify_artwork),
    url(r'upload/$',views.upload_artwork),
    url(r'add/$',views.upload_artwork),
    url(r'comments/(?P<pk>\d+)/$', views.get_comments),
    url(r'comments/delete/(?P<pk>\d+)/$', views.delete_comment),)


