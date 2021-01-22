from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import uuid
from room.models import Room

class Member(models.Model):
    class Meta:
        db_table= 'member'
        ordering = ['id']
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.TextField(null=True, blank=True)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, default=1)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.id.__str__() + " | "+self.name.__str__()