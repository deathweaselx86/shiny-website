#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4
# Create your views here.

from artwork.models import ArtworkModel, CommentModel, shrinkImage
from forms import ArtworkForm

from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic.list import ListView
from django.views.generic import DetailView, TemplateView
from django.views.decorators.csrf import csrf_protect

from django.shortcuts import render_to_response 

from django.db import models

from django.template import RequestContext

from django.contrib.auth.decorators import login_required

#from dajax.core import Dajax
#from dajaxice.decorators import dajaxice_register

# utility method
"""
def create_error_mesage(error_dict):
    problems = list(set(error_dict.values))
    problem_dict = {}
    [problem_dict.setdefault(k, None) for k in problems]
    for k,v in error_dict.iteritems():
        if 

"""

class IndexView(TemplateView):
    template_name = "frontpage.html"

class ArtListView(ListView):
    template_name = 'artwork/artworkmodel_list.html'
    model = ArtworkModel
    paginate_by=10

    def get_context_data(self, **kwargs):
        context = super(ListView,self).get_context_data(**kwargs)
        context['comments'] = CommentModel.objects.all()
        return context

class ArtModelView(DetailView):
    template_name = 'artwork/artworkmodel_detail.html'
    model = ArtworkModel

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['comments'] = CommentModel.objects.filter(artwork=kwargs['object'].id)
        return context

"""
    The next few methods  have something to do with artwork management.

    To manage my artwork successfully, I need:
        - to authenticate, which we can manage with some auth code built into Django
        - to be able to view artwork I've already uploaded in a compact manner
            (it would be nice if I could delete from this page in an AJAX-y manner)
        - a way to modify artwork (and delete)
        - a way to preview and upload artwork

"""
@csrf_protect
@login_required
def upload_artwork(request):
    """
        This view gives you a means of uploading a new piece of artwork.
        It'll even shrink your new piece of artwork if necessary.
    """
    if request.method == 'GET':
        # Then we're coming to the page for the first time.
        # We should display the form associated with this page.
        form = ArtworkForm()
        return render_to_response("artwork/upload.html", 
                                 {"form":form},
                                 context_instance=RequestContext(request))
    
    elif request.method == 'POST':
        # Then we should process the form the user submitted.
        # Validate in Javascript.
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            my_model = form.save()
            # I can't count on this image being where I need it to be
            # until I upload it so I have to save it before shrinking it.
            shrinkImage(my_model)
            return HttpResponseRedirect("/artwork/%s/" % (my_model.id,))
        else:
            return render_to_response("artwork/upload.html",
                                      {"form":form},
                                      context_instance=RequestContext(request))
def compact_view_artwork(request):
    """
        This view shows you all of your artwork, paginated, in a compact manner.
        This view will replace the ArtListView. I want more control over it than the
        generic view will give me.    
        TODO: Give the user the abilities to mass modify/delete artwork.
    """
    pass

@csrf_protect
@login_required
def modify_artwork(request, **kwargs):
    """
        This view allows you to modify the attributes associated with a piece of artwork.
        You may delete a piece of artwork from this page.

        You can also view/delete comments associated with this image.

    """
    artworkModelType = type(ArtworkModel)
    pk = kwargs["pk"]
    # pk is the primary key of the art model we want to change
    if request.method == 'GET':
        # If this is a GET request, we should prepopulate a form with the artwork information.
        # Let's go ahead and reuse the ArtModelForm.
        my_art = ArtworkModel.objects.get(id=pk)
        comments = CommentModel.objects.filter(artwork=pk)
        artForm = ArtworkForm(instance=my_art)
        return render_to_response("artwork/modify.html",
                                 {"form":artForm,
                                  "comments": comments},
                                 context_instance=RequestContext(request))
    else:
        # If this is a POST request, we should take the form data handed to us
        #with the changed form information and resave it. 
        
        # This is real wrong as written right now. Please fix it.
        artForm = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            # If user deleted comments, detect this and delete them.
            # Then save any modifications made to the 
            artForm.save()
            return HttpResponseRedirect("/artwork/%(pk)s/modify/" % locals())
        else:
            return render_to_response("/artwork/modify.html",
                                      {"form": artForm,
                                       "errors": [v[0] for v in artForm.errors.values()],
                                       "comments": comments},
                                      context_instance=RequestContext(request))

