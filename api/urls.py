from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from django.contrib.auth.models import User
from rest_framework import routers
from .views import (RoomViewset,MemberViewset,Startapp,MemberViewsetApi)

router = routers.DefaultRouter()
router.register('room', RoomViewset)
router.register('member', MemberViewset)
urlpatterns = [
    # path('', include(router.urls)),
    path("winner/", Startapp.as_view(), name="winner"),
    path("lobby/", MemberViewsetApi.as_view(), name="lobby_members"),
]
urlpatterns += router.urls