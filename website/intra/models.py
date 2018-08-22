
from django.db import models
# from django.urls import reverse


class Register(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    program = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name + '-' + self.email


class Contact(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name + '-' + self.email
