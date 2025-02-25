from django.db import models

class recom(models.Model):

  place = models.CharField(max_length=255)
  expence = models.IntegerField()
    

# Create your models here.
