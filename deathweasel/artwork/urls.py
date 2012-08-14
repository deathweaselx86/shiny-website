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
    url(r'^(?P<pk>\d+)$', views.ArtModelView.as_view(model=views.ArtworkModel)), 
    # This leads to the page that allows an artist to modify or delete their artwork.
    url(r'modify/(?P<pk>\d+)$', views.modify_artwork),
    url(r'upload$','upload_artwork'),
    url(r'comments/(?P<pk>\d+)$', views.get_comments),)

