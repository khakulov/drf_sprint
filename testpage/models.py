# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class House(models.Model):
    location = models.CharField(max_length=64)
    description = models.CharField(max_length=256)


class Animal(models.Model):
    family = models.CharField(max_length=30)
    email_address = models.EmailField(unique=True)
    name = models.CharField(max_length=32, unique=True)
    secret_key = models.CharField(max_length=32, unique=True)
    house = models.ForeignKey(House, null=True)
