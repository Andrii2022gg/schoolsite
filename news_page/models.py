from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=120)

    text = models.TextField()

    image1 = models.ImageField(upload_to='images/')

    image2 = models.ImageField(upload_to='images/')

    image3 = models.ImageField(upload_to='images/')

    image4 = models.ImageField(upload_to='images/')

    image5 = models.ImageField(upload_to='images/')


    date = models.DateTimeField()

    def __str__(self):
        return self.title

# Create your models here.
