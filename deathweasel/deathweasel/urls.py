from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import django.contrib.auth.views
import artwork.urls
admin.autodiscover()
from artwork.views import IndexView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^artwork/', include(artwork.urls)), 
    url(r'^login/$', django.contrib.auth.views.login),
    url(r'^logout/$', django.contrib.auth.views.logout, 
        {'next_page':'/'}),
    url(r'^logout_redirect/$', django.contrib.auth.views.logout_then_login, 
        {'login_url':'/login/'}),
    url(r'^password_change/$', django.contrib.auth.views.password_change, 
        {'post_change_redirect':'/login/'})

    )
