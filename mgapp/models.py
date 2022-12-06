from django.db import models

# Create your models here.

class Movies(models.Model):
    name=models.CharField(max_length=250)
    dec=models.TextField()
    Year=models.IntegerField()
    Img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name