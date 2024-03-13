from django.db import models

class data(models.Model):
    name = models.CharField(max_length=255)
    number= models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)