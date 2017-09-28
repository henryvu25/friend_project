# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models


class FriendManager(models.Manager):
	def creator(self, postData):
		friend = self.create(first_name=postData['first_name'],last_name=postData['last_name'],alias=postData['alias'],email=postData['email'])
		return friend
	def relate(self, user, friend):
		add = user.friends.add(friend)
		return add
	def forceFriend(self, forceFriend, forceUser):
		force = forceFriend.friends.add(forceUser)
		return force
	def unfriend(self, user, friend):
		unf = user.friends.remove(friend)
		return unf
	def loseFriend(self, lostFriend, lostUser):
		lost = lostFriend.friends.remove(lostUser)
		return lost
	def noFriends(self, user):
		message = {}
		if len(user.friends.all()) < 1:
			message['alert'] = "You don't have any friends yet! Add some!"
		return message


class Friend(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	users = models.ManyToManyField(User, related_name= "friends")
	objects = FriendManager()
