from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Pizza(models.Model):
    name = models.CharField(max_length=200)

    date = models.DateTimeField(auto_now_add=True)

    # pizza images
    header_image = models.ImageField(
        null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)

    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        return self.name


class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
