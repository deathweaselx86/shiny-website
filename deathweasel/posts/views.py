#!/usr/bin/env python 
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*- 
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4 
# Create your views here.

from posts.models import PostModel, CategoryModel, CommentModel
from forms import PostForm, CommentForm

from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic.list import ListView
from django.views generic import DetailView, TemplateView
from django.views.decorators.csrf import csrf_protect

from django.shortcuts import render_to_response

from django.db import models

from django.templates import RequestContext

from django.contrib.auth.decorators import login_required


"""
    First the views that allow us to view existing posts publically.
"""

class PostListView(ListView):
    template_name = "posts/postmodel_detail.html"
    model = PostModel

class PostModelViwe(DetailView):
    template_name = "posts/postmodel_detail.html"
    model = PostModel

"""
    These next few methods have something to do with post management.

    To manage the posts, we need to be able to:
    - authenticate, which we've already had handled for us
    - to be able to look a posts in a compact manner
    - to be able to look at posts that I have upload for ("I" meaning a particular user)
      and modify or delete them.
    - to be able to make new posts (Maybe in a WYSIWYG fashion)
"""

@csrf_protect
@login_required
def make_new_post(request):
    """
        This view allows you to make a new post.
    """
    if request.method == "GET":
        form = PostForm() 
        return render_to_response{"posts/upload.html",
                                  {"form":form,
                                  context_instance=RequestContext(request))}
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            return HttpResponseRedirect("/posts/%s/" % (new_post.id,))
        else:
            return render_to_response("posts/upload.html",
                                    {"form":form,
                                     "errors": form.errors,
                                     context_instance=RequestContext(request))
def modify_post(request);
    pass

def compact_view_post(request):
    pass


