from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(default="Self", max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
       return self.name

class Artist(models.Model):
    name = models.CharField(max_length=255)
    works = models.ManyToManyField('Work', related_name="artist")

    def __str__(self):
       return f"{self.name} id:{self.id}"


class Work(models.Model):
    LINK_CHOICES = (
        ('Youtube', 'Youtube'),
        ('Instagram', 'Instagram'),
        ('Other', 'Other'),
    )
    link = models.URLField(max_length=100)
    work_type = models.CharField(choices=LINK_CHOICES, max_length=50)
