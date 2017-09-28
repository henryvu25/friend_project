# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User
from django.shortcuts import render, redirect
from models import Friend
from django.contrib import messages

def  index(request):
	try:
		request.session['id']
	except: 
		return redirect('/')
	user = User.objects.get(id=request.session['id'])
	friends = Friend.objects.exclude(alias=user.alias)
	notFriends = []
	for i in friends:
		if i not in user.friends.all():
			notFriends.append(i)
	alerts = Friend.objects.noFriends(user)
	if alerts:
		for key in alerts:
			messages.error(request, alerts[key])
	context = {
	"user": User.objects.get(id=request.session['id']),
	"others": notFriends,
	}
	return render(request, "friend_app/home.html", context)

def add(request, id):
	try:
		request.session['id']
	except: 
		return redirect('/')
	user = User.objects.get(id=request.session['id'])
	friend = Friend.objects.get(id=id)
	forceFriend = User.objects.get(alias=friend.alias)
	forceUser = Friend.objects.get(alias=user.alias)
	Friend.objects.relate(user, friend)
	Friend.objects.forceFriend(forceFriend, forceUser)
	return redirect('/index')

def display(request, id):
	try:
		request.session['id']
	except: 
		return redirect('/')
	context = {
	"friend": Friend.objects.get(id=id)
	}
	return render(request, "friend_app/display.html", context)

def remove(request, id):
	try:
		request.session['id']
	except: 
		return redirect('/')
	user = User.objects.get(id=request.session['id'])
	friend = Friend.objects.get(id=id)
	lostFriend = User.objects.get(alias=friend.alias)
	lostUser = Friend.objects.get(alias=user.alias)
	Friend.objects.unfriend(user, friend)
	Friend.objects.loseFriend(lostFriend, lostUser)
	return redirect('/index')

def logout(request):
	request.session.flush()
	return redirect('/')