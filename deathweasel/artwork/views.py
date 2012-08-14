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

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User
#from dajax.core import Dajax
#from dajaxice.decorators import dajaxice_register

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
    
    else:
        # Then we should process the form the user submitted.
        # Validate in Javascript.
        t = request.session.keys()
        z = request.session.items()
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            my_model = form.save()
            # I can't count on this image being where I need it to be
            # until I upload it so I have to save it before shrinking it.
            shrinkImage(my_model)
            return HttpResponseRedirect("artwork/%s/" % (my_model.id,))
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
    # First get all ArtModels.
    # Pass to Paginator.
    all_art_models = ArtModel.objects.all()
    paginator = Paginator(contact_list, 20)

    page = request.GET.get('page')
    try:
        art_models = paginator.page(page)
    except PageNotAnInteger:
        art_models = paginator.page(1)
    except EmptyPage:
        art_models = paginator.page(paginator.num_pages)
    
    return render_to_response('artwork/compact.html', 
                              {'objects':art_models})
@csrf_protect
@login_required
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
        my_art = ArtworkModel.objects.get(id=pk)
        art_form = ArtworkForm(instance=my_art)
        return render_to_response("artwork/modify.html",
                                 {"form":art_form},
                                 context_instance=RequestContext(request))
    else:
        # If this is a POST request, we should take the form data handed to us
        #with the changed form information and resave it. 
        
        art_form = ArtworkForm(request.POST, request.FILES)
        
        if art_form.is_valid():
        # Hopefully this deletes the comments associated with the image as well.
            delete_artwork = art_form.cleaned_data['deleteImage']
            if delete_artwork:
                my_art = ArtworkModel.objects.get(id=pk)
                my_art.delete()
                return HttpResponseRedirect("artwork/")
        # Find a way to delete the comments in an AJAX-y manner!
            # Then save any modifications made to the ArtModel itself. 
            art_form.save()
            return HttpResponseRedirect("artwork/%(pk)s/modify/" % locals())
        else:
            return render_to_response("artwork/modify.html",
                                      {"form": art_form,
                                       "comments": comments},
                                      context_instance=RequestContext(request))

@login_required
def get_comments(request, **kwargs):
    """
        This method retrieves the comment associated with the artwork pk.
    """
    
    pk = kwargs["pk"]   
    these_comments = CommentModel.objects.filter(artwork=pk)
    return render_to_response("artwork/comments.html",
                               {"comments": these_comments})

