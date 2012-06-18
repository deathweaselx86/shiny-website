#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4
"""
This module enables the administration of artwork and comment objects in the
Django admin interface.

"""
from artwork.models import ArtworkModel, CommentModel
from django.db import models
from django.contrib import admin

from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django.conf import settings
from PIL import Image
import os
    
def thumbnail(image_path):
    absolute_url = os.path.join(settings.MEDIA_URL, image_path)
    return '<img src="%s" alt="%s"/>' % (absolute_url, image_path)


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        file_name = str(value)
        if file_name:
            file_path = '%s%s' % (settings.MEDIA_URL, file_name)
            try:
                Image.open(os.path.join(settings.MEDIA_ROOT, file_name))
                output.append('<a target="_blank" href="%s">%s</a><br />%s <a target="_blank" href="%s">%s</a><br />%s ' % (file_path, thumbnail(file_name), _('Currently:'), file_path, file_name, _('Change:')))
            except IOError: # not image
                output.append('%s <a target="_blank" href="%s">%s</a> <br />%s ' % (_('Currently:'), file_path, file_name, _('Change:')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))

class ArtworkAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.ImageField: {'widget': AdminImageWidget},
            }
admin.site.register(CommentModel)
admin.site.register(ArtworkModel)
#admin.site.register(ArtworkModel, ArtworkAdmin)
