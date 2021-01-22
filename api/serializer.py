from django.contrib.auth.models import User
from rest_framework import serializers
from django.apps import apps
iroom = apps.get_model('room', 'Room')
imember = apps.get_model('member', 'Member')

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = iroom
        fields = "__all__"

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = imember
        fields = "__all__"