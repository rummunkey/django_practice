# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def index(request):
	print request
	return render(request, 'make_one/index.html')


def about(request):
	return render(request, 'make_one/about.html')

def projects(request):
	return render(request, 'make_one/projects.html')

def testimonials(request):
	return render(request, 'make_one/testimonials.html')
