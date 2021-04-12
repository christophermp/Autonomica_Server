from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Screen(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    enabled = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Device(models.Model):
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    port = models.CharField(max_length=100)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Macro(models.Model):

    CATEGORY = (
        ('p', 'Projector'),
        ('s', 'Sound'),
        ('a', 'Audiotorium'),
        ('m', 'MediaBlock'),
    )
    name = models.CharField(max_length=100)
    command = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    termination = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY, default='p',)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
