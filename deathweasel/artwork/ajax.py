#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form 

from artwork import models, forms

@dajaxice_register
def test(request):
    dajax = Dajax()
    dajax.alert("test")
    return dajax.json()

@dajaxice_register
def add_comment(request, form):
    dajax = Dajax()
    form = forms.CommentForm(deserialize_form(form))

    if form.is_valid():
        new_comment = form.save()
    
    if new_comment:
        dajax.assign("#commentstatus", 'value', "Comment is successfully added!")
    else:
        dajax.assign("#commentstatus", 'value', "Something went wrong when adding the comment. Try again in a few seconds.")

    return dajax.json()
