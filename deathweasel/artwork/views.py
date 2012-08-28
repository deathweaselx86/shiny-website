#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4
# Create your views here.

from artwork.models import ArtworkModel, CommentModel, shrinkImage
from forms import ArtworkForm, ModifyForm

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

class ArtListView(ListView):
    template_name = 'artwork/artworkmodel_list.html'
    model = ArtworkModel
    paginate_by=30

class ArtModelView(DetailView):
    template_name = 'artwork/artworkmodel_detail.html'
    model = ArtworkModel

def view_art_by_medium(request, **kwargs):
    """
        This view allows you to view artwork based on medium.
    """
    medium = kwargs['medium']
    # Get artwork based on medium
    medium_artwork = ArtworkModel.objects.filter(medium=medium)
    return render_to_response("artwork/filtered_artwork.html",
                             {"filter": medium,
                              "filter_type": "medium"},
                             context_instance=RequestContext(request))

"""
    The next few functions  have something to do with artwork management.

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
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            my_model = form.save(commit=False)
            my_model.artist = request.user
            my_model.save()
            # I can't count on this image being where I need it to be
            # until I upload it so I have to save it before shrinking it.
            shrinkImage(my_model)
            return HttpResponseRedirect("/artwork/%s" % (my_model.id,))
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
        modify_form = populate_modify_form(my_art)
        return render_to_response("artwork/modify.html",
                                 {"form":modify_form,
                                  "pk": pk},
                                 context_instance=RequestContext(request))
    else:
        # If this is a POST request, we should take the form data handed to us
        #with the changed form information and resave it. 
        
        modify_form = ModifyForm(request.POST, request.FILES)
        if modify_form.is_valid():
        # Hopefully this deletes the comments associated with the image as well.
            # If the delete checkbox is selected, delete it
            if modify_form.cleaned_data['delete_art']:
                my_art = ArtworkModel.objects.get(id=pk).delete()
                HttpResponseRedirect("http://www.deathweasel.com/artwork/")
            else:
                my_art = populate_artmodel(modify_form, pk)
                my_art.save()
                HttpResponseRedirect("http://www.deathweasel.com/artwork/%s/" % (pk,))
        else:
        # Recycle the form.
            return render_to_response("artwork/modify.html",
                                     {"form":modify_form,
                                      "pk": pk},
                                     context_instance=RequestContext(request))

# Fill the modify artwork form.
def populate_modify_form(art_model):
    """
        This function populates the ModifyForm with the appropriate contents of
        the corresponding ArtModel.
    """
    artmodel_attrs = ('title', 'artist', 'medium','desc','keywords')
    data = {}
    for attr in artmodel_attrs:
        art_model_string = '.'.join(('art_model', attr))
        data[attr] = eval(art_model_string)
    image = {'image': art_model.image}
    return ModifyForm(data, image)

def populate_artmodel(modify_form, pk):
    """
        This function takes data in the ModifyForm and puts it in the ArtModel in
        anticipation of saving it.
    """
    my_art = ArtworkModel.objects.get(id=pk)
    for key, value in modify_form.iteritems():
        if key == 'delete_art':
            continue
        my_art.setattr(key,value)
    return my_art

# The rest of this crap is primitive ajax.
def delete_comment(request, **kwarg):
    """
        This function selectively deletes a comment based on the comment
        unique id.
    """
    pk = kwarg["pk"]
    comment = CommentModel.objects.get(id=pk)
    comment.delete()
    # Whatever. I'm not going to do anything with this output.
    return HttpResponseRedirect("artwork/" % locals())


def get_deletable_comments(request, **kwargs):
    """
        This function retrieves the comment associated with the artwork pk.
    """
    
    pk = kwargs["pk"]   
    these_comments = CommentModel.objects.filter(artwork=pk)
    return render_to_response("artwork/comments_modify.html",
                               {"comments": these_comments})

def get_comments(request, **kwargs):
    """
        This function retrieves the comment associated with the artwork pk.
    """
    
    pk = kwargs["pk"]   
    these_comments = CommentModel.objects.filter(artwork=pk)
    return render_to_response("artwork/comments.html",
                               {"comments": these_comments})

