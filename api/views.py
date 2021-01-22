from django.shortcuts import render
from rest_framework import permissions, viewsets
from .serializer import (RoomSerializer,MemberSerializer)


# importing apps
from django.apps import apps
iroom = apps.get_model('room', 'Room')
imember = apps.get_model('member', 'Member')


class RoomViewset(viewsets.ModelViewSet):
    queryset = iroom.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoomSerializer

class MemberViewset(viewsets.ModelViewSet):
    queryset = imember.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MemberSerializer