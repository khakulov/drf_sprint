# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Animal(models.Model):
    family = models.CharField(max_length=30, unique=True)
    email_address = models.EmailField(unique=True)
    name = models.CharField(max_length=32, unique=True)
    secret_key = models.CharField(max_length=32, unique=True)
