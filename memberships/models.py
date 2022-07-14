from django.db import models

# Create your models here.

class MembershipType(models.Model):
    membership_title = models.CharField(max_length=200)
    membership_description = models.TextField()
    membership_duration = models.CharField(max_length=2)
    membership_start = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.membership_title