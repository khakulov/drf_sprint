# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import Animal


class ListAnimals(generics.ListAPIView):
    """ List Animals in the system with pagination.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        names = [a.name for a in Animal.objects.all()]
        return Response(names)
