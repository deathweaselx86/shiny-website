#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4

""" This file contains models common to two or more apps."""

from django.db import models
from django.conf import settings

class BaseCommentModel(models.Model):
    """
        This object is the base comment model.
    """
    author = models.CharField(max_length=200, blank=False)
    title = models.CharField(max_length=250)
    body = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    parent = models.OneToOneField("self", null=True)
                                    
    class Meta:
        abstract = True
        ordering = ["-date"]

class KeywordModel(models.Model):
    """
        This class is here so we can search artwork on keywords.
    """
    keyword = models.CharField(max_length=200, blank=False)

    def __unicode__(self):
        return self.keyword

    # Absolute url here should be a link to search on keyword
