#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4

"""
This module contains tests for the artwork module.
>_> Should have wrote all of these before I did anything...
Mea culpa.

"""

from django.test import LiveServerTestCase
from selenium import webdriver


class ArtworkTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()
    
    # Can we get to where we should be able to from
    # the front page?
    def can_view_front_page(self):
        self.browser.get(self.live_server_url)
        title = self.browser.find_element_by_tag('title')
        self.assertIn("deathweasel.net",title)
    
    def can_access_artwork_page(self):
        self.browser.get(self.live_server_url)
        artwork = self.browser.find_element_by_link_text("Artwork")

