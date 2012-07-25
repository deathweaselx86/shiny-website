#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4
# Create your views here.

from artwork.models import ArtworkModel
from forms import ArtworkForm, CommentForm

from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic.list import ListView
from django.views.generic import DetailView, TemplateView
from django.views.decorators.csrf import csrf_protect

from django.shortcuts import render_to_response 
from django.db import models
from django.template import RequestContext


from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

class IndexView(TemplateView):
    template_name = "frontpage.html"

class ArtListView(ListView):
    template_name = 'artwork/artworkmodel_list.html'
    model = ArtworkModel
    paginate_by=10

class ArtModelView(DetailView):
    template_name = 'artwork/artworkmodel_detail.html'
    model = ArtworkModel

"""
    This class contains view methods that have something to do with artwork management.

    To manage my artwork successfully, I need:
        - to authenticate, which we can manage with some auth code built into Django
        - to be able to view artwork I've already uploaded in a compact manner
            (it would be nice if I could delete from this page in an AJAX-y manner)
        - a way to modify artwork (and delete)
        - a way to preview and upload artwork

"""
@csrf_protect
def upload_artwork(request):
    """
        This view gives you a means of uploading a new piece of artwork.
        It will automatically make thumbnails when it saves the model.
    """
    if request.method == 'GET':
        # Then we're coming to the page for the first time.
        # We should display the form associated with this page.
        form = ArtworkForm()
        return render_to_response("artwork/upload.html", 
                                 {"form":form,},
                                 context_instance=RequestContext(request))
    
    elif request.method == 'POST':
        # Then we should process the form the user submitted.
        # Validate in Javascript.
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/artwork/")

def compact_view_artwork(request):
    """
        This view shows you all of your artwork, paginated, in a compact manner.
        This view will replace the ArtListView. I want more control over it than the
        generic view will give me.    
        TODO: Give the user the abilities to mass modify/delete artwork.
    """
    pass

@csrf_protect
def modify_artwork(request, **kwargs):
    """
        This view allows you to modify the attributes associated with a piece of artwork.
        You may delete a piece of artwork from this page.

        You can also view/delete comments associated with this image.

    """
    pk = kwargs["pk"]
    # pk is the primary key of the art model we want to change
    if request.method == 'GET':
        # If this is a GET request, we should prepopulate a form with the artwork information.
        # Let's go ahead and reuse the ArtModelForm.
        my_model = ArtworkModel(id=pk).objects[0]
        form = ArtworkForm(instance=my_model)
        return render_to_response("artwork/modify.html",
                                 {"form":form,},
                                 context_instance=RequestContext(request))
    else:
        # If this is a POST request, we should take the form data handed to us with the
        # changed form information and resave it. 
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/artwork/%(pk)s/modify/" % locals())


