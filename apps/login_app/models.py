# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from django.db import models


class UserManager(models.Manager):
	def creator(self, postData):
		user = self.create(first_name=postData['first_name'],last_name=postData['last_name'],alias=postData['alias'],email=postData['email'],password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()),dob=postData['date'])
		return user

	def loginVal(self, postData):
		errors = {}
		user = self.filter(email=postData['email'])
		if len(user) < 1:
			errors['user'] = "login/password incorrect"
		elif not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
			errors['password'] = "login/password incorrect."
		return errors
		
	def validator(self, postData):
		errors = {}
		user = self.filter(email = postData['email'])
		if not postData['date']:
			errors['date'] = "Date of birth required"
		if user:
			errors['exist'] = "Email already exists."
		for key in postData:
			if re.search(" ", postData[key]):
				errors['spaces'] = "Spaces not allowed."
		if len(postData['first_name']) < 2:
			errors['first_name'] = "First name must have at least 2 characters."
		if len(postData['last_name']) < 2:
			errors['last_name'] = "last name must have at least 2 characters."
		if len(postData['alias']) < 2:
			errors['alias'] = "Alias must have at least 2 characters."
		if not re.match("[^@]+@[^@]+\.[^@]+", postData['email']):
			errors['email'] = "Email not valid."
		if postData['password'] != postData['c_password']:
			errors['match'] = "Password does not match."
		if len(postData['password']) < 8:
			errors['password'] = "Password must have at least 8 characters."
		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	dob = models.DateField()
	objects = UserManager()
