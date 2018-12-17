#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 11:01:51 2018

@author: walace
"""

from django.conf.urls import url
from perfis.views import index, exibir

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^perfis$', exibir, name='exibir')
]