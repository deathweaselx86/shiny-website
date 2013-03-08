#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def test(request):
    dajax = Dajax()
    dajax.alert("test")
    return dajax.json()
