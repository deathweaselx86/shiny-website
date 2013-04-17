#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4

from dajax.core import Dajax
from dajaxice.utils import deserialize_form 
from dajaxice.decorators import dajaxice_register

from artwork import models, forms




@dajaxice_register
def test(request):
    dajax = Dajax()
    dajax.alert("alert")
    return dajax.json()

@dajaxice_register
def add_comment(request, form):
    dajax = Dajax()
    form = forms.CommentForm(deserialize_form(form))
    
    new_comment = None
    if form.is_valid():
        new_comment = models.CommentModel.objects.create(**form.cleaned_data)
    
    if new_comment:
        dajax.add_data("Comment is successfully added!", "commentStatus")
    else:
        # Add more information here....
        dajax.add_data("Something went wrong with adding the comment.", "commentStatus")
    
    return dajax.json()

""""
@dajaxice_register
def get_comments(request, pk):
    these_comments = models.CommentModel.objects.filter(artwork=pk)
    if these_comments:
        i=0
        for comment in these_comments:
            i=i+1
            dajax.add_data("comment_info"
    else:

    return dajax.json()
"""
