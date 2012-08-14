#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4
from models import ArtworkModel, CommentModel
from django.forms import ModelForm


class ArtworkForm(ModelForm):
    class Meta:
        model=ArtworkModel
        exclude = ('upload_date',)

class CommentForm(ModelForm):
    class Meta:
        model=CommentModel
        exclude = ('date',)
