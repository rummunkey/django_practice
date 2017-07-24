# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import string

import random

from django.shortcuts import render, redirect

# Create your views here.


def index(request):
	if not 'attempts' in request.session:
		request.session['attempts'] = 0
	return render(request, 'generator/index.html')


def generator(size=14, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


def middle(request):
	request.session['word'] = generator()
	request.session['attempts'] += 1
	# print request.session.word
	return redirect('/')
