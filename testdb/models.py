from django.db import models

class data(models.Model):
    name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    create_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    