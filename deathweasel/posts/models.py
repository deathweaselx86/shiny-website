#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4

from django.db import models
from django.contrib.auth.models import User
from artwork.models import KeywordModel, BaseCommentModel

# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length=250, help_text="Maximum size is 250 characters.")
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=True)
    body = models.TextField(blank=False, help_text="Your post goes here.")
    allow_comments = models.BooleanField(default=False)
    viewable = models.BooleanField(default=False)
    category = models.ManyToManyField(KeywordModel)

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['-date']
    
    # There is another, better way to do this, but I'm out of
    # time to get it to work properly.
    def get_absolute_url(self):
        return "/posts/%s/" % self.id

class CommentModel(BaseCommentModel):
    post = models.ForeignKey(PostModel)
    parent = models.OneToOneField("self", null=True)    
   
    class Meta(BaseCommentModel.Meta):
        db_table = "posts_commentmodel"
