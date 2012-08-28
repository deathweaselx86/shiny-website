#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4
"""
This module enables the administration of artwork and comment objects in the
Django admin interface.

"""
from artwork.models import ArtworkModel, CommentModel, KeywordModel
from django.db import models
from django.contrib import admin

from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django.conf import settings
from PIL import Image
import os
    
admin.site.register(CommentModel)
admin.site.register(ArtworkModel)
admin.site.register(KeywordModel)
