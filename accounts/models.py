# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length = 100,blank=True)
    comments = models.TextField(max_length = 100,blank=True)
    birth_date = models.DateField(null=True,blank=True)
    image = models.FileField(null=True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

def create_profile(sender,**kwargs):
    if kwargs['created']:
        userprofile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender= User)
