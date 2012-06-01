#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4
from django.db import models

# Create your models here.
def getFilePath(instance, filename):
    """
        This makes a hopefully unique filename by hashing together
        a string formed of the upload_date, artist, and filename.
        We then return a string representing the url that the file goes to.
    """
    file_extension = filename.split('.')[1]

    hash_string = hash(''.join((str(instance.title), str(instance.artist),\
        filename)))
    hash_string = str(hash_string).replace('-','')
    return 'images/%s/%s.%s' % (str(instance.medium), hash_string, file_extension)

	
class ArtworkModel(models.Model):
    """
        This class contains the information necessary to describe a piece of
        artwork uploaded to my website. Technically, the artist field is
        unnecessary, but I'm throwing it in because I'd like to be able
        to upload collaborations.
    """
    MEDIUMS = (('ink', 'ink'),
               ('graphite', 'graphite'),
               ('watercolor', 'watercolor'),
               ('oil', 'oil'),
               ('acrylic', 'acrylic'),
               ('digital', 'digital'),
               ('sculpture', 'sculpture'),
               ('other','other'))

    title = models.CharField(max_length=200)
    medium = models.CharField(max_length=200, choices=MEDIUMS, default='graphite')
    upload_date = models.DateTimeField(auto_now_add=True)
    artist = models.CharField(max_length=200)
    image = models.ImageField(upload_to=getFilePath)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return '-'.join((self.title, self.artist, self.medium))

class CommentModel(models.Model):
    """
        This class contains the information necessary to describe a comment
        that someone's left about a piece of artwork. 
    """
    commenteer = models.CharField(max_length=200, blank=False)
    comment_body = models.TextField(blank=False)
    artwork = models.ForeignKey(ArtworkModel)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']
