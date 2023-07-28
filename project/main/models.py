from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField(blank=False)
    
    def __str__(self):
        return self.title