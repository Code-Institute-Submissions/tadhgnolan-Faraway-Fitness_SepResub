from django.db import models
import random

# Create your models here.


class Welcome(models.Model):
    welcome_title = models.CharField(max_length=200)
    welcome_content = models.TextField()

    def __str__(self):
        return self.welcome_title

    def get_random():
        return Welcome.objects.order_by("?").first()


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email
