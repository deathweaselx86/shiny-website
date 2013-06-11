#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from core.models import BaseCommentModel, KeywordModel

MEDIUMS = (('ink', 'ink'),
               ('graphite', 'graphite'),
               ('watercolor', 'watercolor'),
               ('oil', 'oil'),
               ('acrylic', 'acrylic'),
               ('digital', 'digital'),
               ('sculpture', 'sculpture'),
               ('other','other'))

# Create your models here.
def getFilePath(instance, filename):
    """
        This makes a hopefully unique filename by hashing together
        a string formed of the upload_date, artist, and filename.
        We then return a string representing the url that the file goes to.
    """
    import time

    file_extension = filename.split('.')[1]
    
    hash_string = hash(''.join((str(instance.title), time.ctime(), filename)))
    hash_string = str(hash_string).replace('-','')
    return 'images/%s/%s.%s' % (str(instance.medium), hash_string, file_extension)

def shrinkImage(artmodel):
    """

    This shrinks the initial images when you upload them so you don't just have huge images 
    hanging out in the file system..
    
    """

    # This can be written more efficiently. Please look into it.

    from PIL import Image
    import tempfile
    from django.core.files.images import ImageFile
    from django.core.files.storage import default_storage

    image = artmodel.image
    pil_image = Image.open(image)
    
    # Here's our current height and width.
    current_width, current_height = pil_image.size
    
    if current_width > 800:
        # Resize due to width.
        new_width = 800
        new_height = int(current_height*((1.0*new_width)/current_width))
    elif current_height > 1200:
        # Resize due to height.
        new_height = 1200
        new_width = int(current_width*((new_height*1.0)/current_height))
    else:
        # Otherwise the sizing is good.
        return
    pil_image = pil_image.resize((new_width, new_height), Image.ANTIALIAS)

    # Delete the image associated with the ImageField. Don't worry, we
    # will replace it shortly.
    filename = settings.MEDIA_ROOT + image.name

    # Create new image and save the resized image to it.
    with tempfile.NamedTemporaryFile() as tempfile:
        pil_image.save(tempfile, 'JPEG', quality=90)
        artmodel.image.save(filename, ImageFile(tempfile), save=True)

class ArtworkModel(models.Model):
    """
        This class contains the information necessary to describe a piece of
        artwork uploaded to my website. Technically, the artist field is
        unnecessary, but I'm throwing it in because I'd like to be able
        to upload collaborations.
    """
    
    title = models.CharField(max_length=200)
    medium = models.CharField(max_length=200, choices=MEDIUMS, default='graphite')
    upload_date = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(User)
    image = models.ImageField(upload_to=getFilePath)
    desc = models.TextField(verbose_name="Description", max_length=500)
    keywords = models.ManyToManyField(KeywordModel)
    
    class Meta:
        ordering = ["title"]

    def __unicode__(self):
        return '-'.join((self.title, self.artist.username, self.medium))

    def get_absolute_url(self):
        return "/artwork/%s/" % self.id

class CommentModel(BaseCommentModel):
    """
        This class contains the information necessary to describe a comment
        that someone's left about a piece of artwork. 
    """
    artwork = models.ForeignKey(ArtworkModel)

    def __unicode__(self):
        return ' '.join((self.author, self.title, "on", self.title))
    
    class Meta(BaseCommentModel.Meta):
        db_table = "artwork_commentmodel"    
    
