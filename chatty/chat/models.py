from django.core.checks import messages
from django.db import models

from account.models import User


class Room(models.Model):
    room_name = models.CharField(max_length=25, unique=True, blank=True)
    room_password = models.CharField(max_length=15, blank=True)
    room_created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('room_created_date',)



class Message(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    # room = models.CharField(max_length=255)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.TextField()
    message_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('message_time',) 
    
    def __str__(self) -> str:
        return f'{self.room}->{self.username}'