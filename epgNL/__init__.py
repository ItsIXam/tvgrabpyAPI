#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python 3 compatibility
from __future__ import unicode_literals
# from __future__ import print_function

from .tv_grab_config import *

__version__  = '%s.%s.%s' % (API_MAJOR,API_MINOR,API_PATCH)
if API_ALPHA:
    __version__ = '%s-alfa' % (__version__)

elif API_BETA:
    __version__ = '%s-beta' % (__version__)

def version():
    return (API_NAME, API_MAJOR, API_MINOR, API_PATCH, API_PATCHDATE, API_BETA, API_ALPHA)

