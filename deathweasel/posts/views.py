#!/usr/bin/env python 
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*- 
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4 
# Create your views here.

from artwork.models import KeywordModel
from posts.models import PostModel, CommentModel
from forms import PostForm, CommentForm, ModifyForm

from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic.list import ListView
from django.views.generic import DetailView, TemplateView
from django.views.decorators.csrf import csrf_protect

from django.shortcuts import render_to_response

from django.db import models

from django.template import RequestContext

from django.contrib.auth.decorators import login_required


"""
    First the views that allow us to view existing posts publically.
"""

class PostListView(ListView):
    template_name = "posts/postmodel_list.html"
    model = PostModel

class PostModelView(DetailView):
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
def add_post(request):
    """
        This view allows you to make a new post. If you mess up somewhere and submit,
        it will start you on the same page with your content. Hopefully we'll validate
        everything in Javascript.
    """
    if request.method == "GET":
        form = PostForm() 
        return render_to_response("posts/add.html",
                                  {"form":form},
                                  context_instance=RequestContext(request))
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            form.save_m2m()
            return HttpResponseRedirect("/posts/%s/" % (new_post.id,))
        else:
            return render_to_response("posts/add.html",
                                      {"form":form},
                                      context_instance=RequestContext(request))

@csrf_protect
@login_required
def modify_post(request, **kwargs):
    """
        This view allows you to modify a post. You may delete the post from this page.
        
        You can also view or delete comments from this post.
    """
    pk = kwargs['pk']
    if request.method == 'GET':
        my_post = PostModel.objects.get(id=pk)
        post_form = ModifyForm(instance=my_post)
        return render_to_response("posts/modify.html",
                                {"form":post_form,
                                 "pk":pk},
                                context_instance=RequestContext(request))
    else:
        my_post = PostModel.objects.get(id=pk)
        post_form = ModifyForm(request.POST, instance=my_post)
        if post_form.is_valid():
            delete_post = post_form.cleaned_data['delete_post']
            if delete_post:
                my_post.delete()
                return HttpResponseRedirect("/posts/")
            else:
                post_form.save()
                return HttpResponseRedirect("/posts/%(pk)s/" % locals())
        else:
            return render_to_response("posts/modify.html",
                                      {"form": post_form, 
                                        "pk": pk,
                                        "errors": post_form.errors},
                                      context_instance=RequestContext(request))


