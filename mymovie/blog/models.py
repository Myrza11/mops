# from mymovie.mymovie.settings import DEBUG
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import BaseExpression
# from django.db.models.fields import BinaryField, CharField, DateTimeField, EmailField, IntegerField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)
    descripton = models.TextField()
    url = models.SlugField(max_length=255)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    url = models.SlugField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(upload_to='photos/%Y/%m/%d')
    year = models.DateTimeField()
    country = models.CharField(max_length=255)
    derictory = models.ForeignKey(Actor, on_delete=models.CASCADE, verbose_name='DIRECTOR',related_name='directory', default=True)
    actory = models.ForeignKey(Actor, on_delete=models.CASCADE, verbose_name='ACTOR',related_name='actor', default=False)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    world_premiere = models.DateTimeField()
    budget = models.IntegerField()
    fees_in_country = models.IntegerField()
    fees_in_world = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ds')
    # star = models.ForeignKey('Rating', on_delete=models.CASCADE, verbose_name='star',related_name='s', default=True)
    url = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Rating(models.Model):
    STAR = [
        ('1', "1"),
        ('2', "2"),
        ('3', "3"),
        ('4', "4"),
        ('5', "5"),
    ]
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=STAR, default='5')

    def __str__(self):
        return self.type


class MovieImage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')

    def __str__(self):
        return self.title

class Review(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)

    def __str__(self):
        return self.email