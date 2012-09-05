#!/usr/bin/env python 
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*- 
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4 
# Create your views here.
from django.conf.urls import patterns, include, url
from posts import views
from posts.models import PostModel


urlpatterns = patterns('posts.views',
    # This leads to the page that say there's art here!
    # This also shows a paginated view of all artwork.
    url(r'^$', views.PostListView.as_view(model=PostModel)), 
    # This leads to the page that shows a particular piece of artwork and
    # comments associated with it. Well, not the comments, yet. 
    url(r'^(?P<pk>\d+)/$', views.PostModelView.as_view(model=PostModel)), 
    # This leads to the page that allows an artist to modify or delete their artwork.
    url(r'modify/(?P<pk>\d+)/$', views.modify_post),
    url(r'add/$',views.add_post))


