from django.db import models

# Create your models here.

class Message(models.Model):
    sender_email = models.EmailField(blank=False, null=False, default='')
    message = models.CharField(max_length=1000, default='', null=True, blank=False)

    def __str__(self):
        return self.message
