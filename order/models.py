from django.db import models
from main.models import Destination, Post


class Order(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                                    related_name='orders')
    phone = models.CharField(max_length=13)
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.email} - {self.phone}'

