#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4
from models import ArtworkModel, KeywordModel, CommentModel, MEDIUMS

from django.contrib.auth.models import User

from django import forms

from django.utils import html 

class ModifyImageInput(forms.ClearableFileInput):
    """
        Here's my attempt to make the widget that's rendered for
        ImageModels look the way I want it to. I'd like it to at least
        SHOW the image rather than a link to it.
    
        I am deliberately leaving out the case of the non-required image field.
        TODO: Can I leverage sorl.thumbnail here?
    """
    def render(self, name, value, attrs=None):
        substitutions = {
                'initial_text': self.initial_text,
                'input_text': self.input_text,
                'clear_template': '',
                'clear_checkbox_label': self.clear_checkbox_label,
        }
        template = '%(input)s'
        substitutions['input'] = super(forms.ClearableFileInput, self).render(name, value, attrs)
        
        if value and hasattr(value, "url"):
            template = self.template_with_initial
            substitutions['initial'] = str.format('<img width="200" src="{0}"/>', value.url)
        return html.mark_safe(template % substitutions)

class ArtworkForm(forms.ModelForm):
    image = forms.ImageField(widget=ModifyImageInput) 
    class Meta:
        model=ArtworkModel
        exclude = ("upload_date", "artist")
        widgets = {"image": ModifyImageInput()}
    class Media:
        js = (
               'http://ajax.aspnetcdn.com/ajax/jquery.validate/1.9/jquery.validate.min.js', 
               'http://ajax.aspnetcdn.com/ajax/jquery.validate/1.9/additional-methods.min.js')

class ModifyForm(forms.Form):
    """
        This form is used for the artwork modify screen.
    """
    # Not done.
    title = forms.CharField(max_length=200)
    artist = forms.ModelChoiceField(queryset=User.objects.all())
    medium = forms.ChoiceField(required=True, choices=MEDIUMS)
    image = forms.ImageField(required=True, widget=ModifyImageInput)
    desc = forms.CharField(max_length=500, widget=forms.Textarea)
    keywords = forms.ModelMultipleChoiceField(queryset=KeywordModel.objects.all())
    delete_art = forms.BooleanField()
    class Media:
         js = (
               'http://ajax.aspnetcdn.com/ajax/jquery.validate/1.9/jquery.validate.min.js', 
               'http://ajax.aspnetcdn.com/ajax/jquery.validate/1.9/additional-methods.min.js')

class CommentForm(forms.ModelForm):
    class Meta:
        model=CommentModel
        exclude = ('date',)
    class Media:
         js = (
               'http://ajax.aspnetcdn.com/ajax/jquery.validate/1.9/jquery.validate.min.js', 
               'http://ajax.aspnetcdn.com/ajax/jquery.validate/1.9/additional-methods.min.js')
