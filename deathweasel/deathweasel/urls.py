from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import artwork.urls
admin.autodiscover()
from artwork.views import IndexView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^artwork/', include(artwork.urls)), 
    )
