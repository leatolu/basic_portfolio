from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # pub_date = models.DateTimeField('date published')
    # expire_date = models.DateTimeField('date expires', null=True)
    # show_public = models.BooleanField(default=False)
    # slides = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=200, unique=True)
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Slide(models.Model):
    # position = models.IntegerField(default=-1)
    # visible = models.BooleanField(default=False)
    images = models.ManyToManyField(Image)
    gallery = models.ForeignKey(Gallery)
