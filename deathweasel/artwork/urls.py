from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('artwork.views',
    # This leads to the page that say there's art here!
    # This also shows a paginated view of all artwork.
    url(r'^artwork/$', 'index'), 
    # This leads to the page that shows a particular piece of artwork and
    # comments associated with it.
    url(r'^artwork/?<title>\d+/$', 'art'), 
)
    
