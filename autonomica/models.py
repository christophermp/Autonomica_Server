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


class Help(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    info = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
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
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    port = models.CharField(max_length=100)
    cinema = models.BooleanField(default=False, blank=True, help_text="If Jnior is Cinema Application installed?")
    tasker = models.BooleanField(default=False, blank=True, help_text="If Jnior is Tasker Application installed?")

    def __str__(self):
        return self.name


class Macro(models.Model):
    CATEGORY = (
        ('p', 'Projector'),
        ('s', 'Sound'),
        ('a', 'Audiotorium'),
        ('m', 'MediaBlock'),
    )
    CATEGORY_JNIOR = (
        ('n', 'None'),
        ('c', 'Cinema Application'),
        ('t', 'Tasker Application'),
    )

    CATEGORY_COLOR_BUTTON = (
        ('danger', 'Red'),
        ('success', 'Green'),
        ('info', 'Blue'),
        ('warning', 'Yellow'),

    )
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, help_text="Related to screen.")
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True, help_text="Device category.")
    name = models.CharField(max_length=100, help_text="Public name.")
    command = models.CharField(max_length=100, help_text="System command.")
    termination = models.CharField(max_length=100, blank=True, help_text="Termination String if any.")
    colors = models.CharField(max_length=20, choices=CATEGORY_COLOR_BUTTON, default='danger',
                              help_text="If you want a other button color you can select it here.")
    category = models.CharField(max_length=100, choices=CATEGORY, default='p', )
    jnior = models.CharField(max_length=100, choices=CATEGORY_JNIOR, default='n',
                             help_text="Use if macro is amed for Tasker or Cinema Application.")

    def __str__(self):
        return self.name


class Task(models.Model):

    CATEGORY_COLOR_BUTTON = (
        ('danger', 'Red'),
        ('success', 'Green'),
        ('info', 'Blue'),
        ('warning', 'Yellow'),

    )

    screen = models.ForeignKey(Screen, null=True, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    colors = models.CharField(max_length=20, choices=CATEGORY_COLOR_BUTTON, default='danger',
                              help_text="If you want a other button color you can select it here.")
    version = models.CharField(max_length=100)
    modified = models.CharField(max_length=100)
    macro_name = models.CharField(max_length=100)
    device = models.CharField(max_length=100)
    type = models.CharField(max_length=100, help_text="If PulseRelay Message section will be an INT representing Rout JNIOR")
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.task_name
