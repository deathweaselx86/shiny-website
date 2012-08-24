#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4
from models import PostModel, CommentModel
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model=PostModel
        exclude = ('date','user')
    class Media:
        js = ('http://ajax.aspnetcdn.com/ajax/jquery.validate/1.9/additional-methods.min.js',\
                'http://ajax.aspnetcdn.com/ajax/jquery.validate/1.9/jquery.validate.min.js')


class CommentForm(ModelForm):
    class Meta:
        model=CommentModel
        exclude = ('date')
    class Media:
        js = ('http://ajax.aspnetcdn.com/ajax/jquery.validate/1.9/additional-methods.min.js',\
                'http://ajax.aspnetcdn.com/ajax/jquery.validate/1.9/jquery.validate.min.js')


