from django.db import models

# Create your models here.

class College_info(models.Model):
    college_name = models.CharField(primary_key=True, max_length=50)
    info = models.TextField()
    established = models.TextField()
    location = models.CharField(max_length=200)