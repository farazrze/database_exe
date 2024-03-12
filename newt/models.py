from django.db import models

class nwt(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    email = models.EmailField()
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['date']


