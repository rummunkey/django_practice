# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse


def index(request):
    printer()
    return render(request, 'first_app/index.html')


def printer():
    print 'hello world'


# Create your views here.
