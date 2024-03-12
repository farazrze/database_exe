from django.db import models

class data(models.Model):
    name=models.CharField(max_length=255)
    last_name=models.TextField()
    create_date=models.DateTimeField(auto_now_add=True)