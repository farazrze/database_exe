from django.db import models

class ex(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)



    def __str__(self):
        return self.name