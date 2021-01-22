from django.shortcuts import render
from rest_framework import permissions, viewsets, generics
from .serializer import (RoomSerializer,MemberSerializer)
from rest_framework.response import Response
import random
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

def get_room(request):
    room = request.GET.get("room")
    qs = iroom.objects.filter(id=room)
    return qs
    

class Startapp(generics.ListAPIView):
    @classmethod
    def get_extra_actions(cls):
        return []
    serializer_class = MemberSerializer
    serializer_rooom = RoomSerializer
    permission_classes = [permissions.AllowAny]

    

    def get_queryset(self):
        room = self.request.GET.get("room")
        qs = imember.objects.filter(room=room)
        return qs

    def list(self, request):
        queryset = self.get_queryset()
        total_people = queryset.count()
        room = get_room(request)
        winner_gift = ((room[0].entry_fee*total_people)*95)/100
        winner = random.choice(queryset)
        serializer = self.serializer_class(winner)
        winner = serializer.data
        return Response({"winner": winner, "gift": winner_gift})

class MemberViewsetApi(generics.ListAPIView):
    @classmethod
    def get_extra_actions(cls):
        return []
    serializer_class = MemberSerializer
    permission_classes = [permissions.AllowAny]

    

    def get_queryset(self):
        room = self.request.GET.get("room")
        qs = imember.objects.filter(room=room)
        return qs

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        member = serializer.data
        return Response(member)