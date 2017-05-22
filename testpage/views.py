# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .serializers import AnimalSerializer


class ListAnimals(generics.ListAPIView):
    """ List Animals in the system with pagination.
    """
    serializer_class = AnimalSerializer
    model = AnimalSerializer.Meta.model
    queryset = model.objects.all()
