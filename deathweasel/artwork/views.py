#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4
# Create your views here.

from artwork.models import ArtworkModel
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic import DetailView, TemplateView

class IndexView(TemplateView):
    template_name = "frontpage.html"

class ArtListView(ListView):
    template_name = 'artwork/artworkmodel_list.html'
    model = ArtworkModel
    paginate_by=10

    def dispatch(self, *args, **kwargs):
        return super(ArtListView, self).dispatch(*args,**kwargs) 
    
class ArtModelView(DetailView):
    pass
