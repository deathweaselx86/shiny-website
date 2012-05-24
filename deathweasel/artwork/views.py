#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4
# Create your views here.

from artwork.models import ArtworkModel
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic import DetailView

class ArtListView(ListView):
    pass


class ArtModelView(DetailView):
    pass
