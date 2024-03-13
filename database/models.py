from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=255)
    number= models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    