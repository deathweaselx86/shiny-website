#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4
"""
This module enables the administration of artwork and comment objects in the
Django admin interface.

"""
from artwork.models import ArtworkModel, CommentModel
from django.contrib import admin

for klass in (ArtworkModel, CommentModel):
    admin.site.register(klass)
