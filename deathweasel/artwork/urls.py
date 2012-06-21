from django.conf.urls import patterns, include, url
from artwork.views import ArtListView, ArtModelView
from artwork.models import ArtworkModel

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('artwork.views',
    # This leads to the page that say there's art here!
    # This also shows a paginated view of all artwork.
    url(r'^$', ArtListView.as_view(model=ArtworkModel)), 
    # This leads to the page that shows a particular piece of artwork and
    # comments associated with it.
    url(r'^(?P<pk>\d+)/$', ArtModelView.as_view(model=ArtworkModel), 
))
    
