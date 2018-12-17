# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse('Bem vindo ao Admin - Usuário Walace da Cunha')
    return render(request,'default.html')


def exibir(request):
    return render(request,'perfil.html')