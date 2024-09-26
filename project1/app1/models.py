from django.db import models
from django.utils import timezone

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    user_name = models.CharField(max_length=50)
    date_added = models.DateTimeField(default = timezone.now)