#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4

from dajax.core import Dajax
from dajaxice.utils import deserialize_form 
from dajaxice.decorators import dajaxice_register

from artwork import models, forms



@dajaxice_register
def add_comment(request, form):
    dajax = Dajax()
    form = forms.CommentForm(deserialize_form(form))
    
    new_comment = None
    if form.is_valid():
        new_comment = models.CommentModel.objects.create(**form.cleaned_data)
    
    if new_comment:
        dajax.add_data("Comment is successfully added!", "commentStatus")
        comment_json = serializers.serialize('json', new_comment)
        djax.add_data(comment_json, 'addNewComment') 
    else:
        # Add more information here....
        dajax.add_data("Something went wrong with adding the comment.", "commentStatus")
    return dajax.json()
    

@dajaxice_register
def get_comments(request, art_pk):
    dajax = Dajax()
    
    comments = models.CommentModel.objects.filter(artwork=art_pk)
    if not comments:
        dajax.add_data('No comments associated with this post.', 'commentStatus')
    else:
        comment_json = serializers.serialize('json', comments)
        # Not implemented yet.
        dajax.add_data(comment_json, 'render_comments')
    return dajax.json()

