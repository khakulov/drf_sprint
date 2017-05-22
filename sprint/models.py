# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Programmer(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    eats_meat = models.BooleanField(default=True)
    from_pdx = models.BooleanField(default=False)
    email = models.EmailField()
