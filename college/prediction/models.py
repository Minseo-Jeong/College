from django.db import models

# Create your models here.

class Predict_list(models.Model):
    college_name = models.CharField(max_length=50)
    major_name = models.CharField(max_length=50)
    cutline = models.IntegerField()
