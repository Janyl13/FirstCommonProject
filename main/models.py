
from django.db import models

# class User(models.Model):
#     name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50, blank=True)
#     phone = models.Model()
#     email = models.EmailField(max_length=50, blank=True)
#     image = models.ImageField(blank=True, null=True, uploud_to='users')
from django.db.models import TextField


class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='authors')

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Category(models.Model):
    slug = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100, unique=True)


class Destination(models.Model):
    slug = models.SlugField(max_length=55, primary_key=True)
    name = models.CharField(max_length=55, unique=True)
    image = models.ImageField(upload_to='destinations')
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='destinations')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.image.url


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = TextField()
    image = models.ImageField(blank=False, null=False, upload_to='posts')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    destination = models.ManyToManyField(Destination)

    def __str__(self):
        return self.title














