from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import redirect_to
from django.conf import settings

import django.contrib.auth.views


import posts.views
import artwork.urls, posts.urls

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', posts.views.PostListView.as_view(model=posts.views.PostModel)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^artwork/', include(artwork.urls)), 
    url(r'^posts/', include(posts.urls)),
    url(r'^login/$', django.contrib.auth.views.login),
    url(r'^logout/$', django.contrib.auth.views.logout, 
        {'next_page':'/'}),
    url(r'^logout_redirect/$', django.contrib.auth.views.logout_then_login, 
        {'login_url':'/login/'}),
    url(r'^password_change/$', django.contrib.auth.views.password_change, 
        {'post_change_redirect':'/login/'}),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    )

urlpatterns += staticfiles_urlpatterns()
