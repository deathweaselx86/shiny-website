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
    return 'images/%s/%s.%s' % (str(instance.medium), hash_string, file_extension)

	
class ArtworkModel(models.Model):
    """
        This class contains the information necessary to describe a piece of
        artwork uploaded to my website. Technically, the artist field is
        unnecessary, but I'm throwing it in because I'd like to be able
        to upload collaborations.
    """
    title = models.CharField(max_length=200)
    medium = models.CharField(max_length=200, default="Ink")
    upload_date = models.DateTimeField(auto_now_add=True)
    artist = models.CharField(max_length=200)
    image = models.ImageField(upload_to=getFilePath)


    def __unicode__(self):
        return '-'.join((self.title, self.artist, self.medium))

    def getFilePath(self, instance, filename):
        """
            This makes a hopefully unique filename by hashing together
            a string formed of the upload_date, artist, and filename.
            We then return a string representing the url that the file goes to.
        """
        file_extension = '.'.split(filename)[1]

        hash_string = hash(''.join((str(instance.title), str(instance.artist),\
            filename)))
        return 'images/%s/%s.%s' % (str(instance.medium), hash_string, file_extension)

class CommentModel(models.Model):
    commenteer = models.CharField(max_length=200, blank=False)
    comment_body = models.TextField(blank=False)
    artwork = models.ForeignKey(ArtworkModel)
