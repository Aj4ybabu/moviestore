from django.db import models

# Create your models here.
class Movie(models.Model):
    img = models.ImageField(upload_to='pics/')
    name=models.CharField(max_length=200)
    desc=models.TextField()
    year=models.IntegerField()



    def __str__(self):
        return self.name