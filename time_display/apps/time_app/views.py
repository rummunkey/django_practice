# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
	now = datetime.datetime.now()
	today = now.strftime("%b %d, %Y")
	time = now.strftime("%I:%M %p")
	context = {
		'day': today,
		'time': time
	}
	return render(request, 'time_app/index.html', context)


def show_time():
	now = datetime.datetime.now()
	print now.strftime('%b %d %Y')
