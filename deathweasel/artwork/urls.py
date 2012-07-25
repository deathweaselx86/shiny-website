from django.conf.urls import patterns, include, url
from artwork import views
from artwork.models import ArtworkModel

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('artwork.views',
    # This leads to the page that say there's art here!
    # This also shows a paginated view of all artwork.
    url(r'^$', views.ArtListView.as_view(model=views.ArtworkModel)), 
    # This leads to the page that shows a particular piece of artwork and
    # comments associated with it. Well, not the comments, yet. 
    url(r'^(?P<pk>\d+)/$', views.ArtModelView.as_view(model=views.ArtworkModel)), 
    # This leads to the page that allows an artist to modify or delete their artwork.
    url(r'^(?P<pk>\d+)/modify/$', views.modify_artwork),)



urlpatterns += patterns('artwork.views',
   (r'upload/$', 'upload_artwork'),)
