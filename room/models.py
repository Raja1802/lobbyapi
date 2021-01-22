from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import uuid

class Room(models.Model):
    class Meta:
        db_table= 'room'
        ordering = ['id']
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    room_name = models.TextField(null=True, blank=True)
    entry_fee = models.IntegerField(default=0)
    total_fee = models.BigIntegerField(default=0)
    winner = models.IntegerField(default=0)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.id.__str__() + " | "+self.room_name.__str__()