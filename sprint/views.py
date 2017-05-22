# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from models import Programmer
from serializers import ProgrammerSerializer


# Create your views here.
class ProgrammerViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
    permission_classes = []
