# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from ..friend_app.models import Friend


def index(request):
	
	return render(request, "login_app/index.html")

def process(request):
	regErrors = User.objects.validator(request.POST)
	if regErrors:
		for key in regErrors:
			messages.error(request, regErrors[key])
		return redirect('/')
	user = User.objects.creator(request.POST)
	friend = Friend.objects.creator(request.POST)
	messages.success(request, "Registration successful! Please log in.")
	return redirect('/')

def login(request):
	loginErrors = User.objects.loginVal(request.POST)
	if loginErrors:
		for key in loginErrors:
			messages.error(request, loginErrors[key])
		return redirect('/')
	request.session['id'] = User.objects.get(email=request.POST['email']).id
	return redirect('/index')