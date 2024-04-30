from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    def __str__(self):
        return self.title

