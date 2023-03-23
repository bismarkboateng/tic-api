from django.db import models
from user.models import User

class Message(models.Model):
    message = models.TextField() 
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE) 
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.receiver.email}"
    