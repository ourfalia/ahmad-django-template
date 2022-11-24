from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



# Create your models here.
class Item(models.Model):
    number = models.CharField(max_length=50, null=False, blank=False)
    booked = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.number