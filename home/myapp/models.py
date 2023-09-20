from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(default="Self", max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
       return self.name



class Rating(models.Model):
    artist = models.ForeignKey('Artist', related_name='rating',
                                on_delete=models.CASCADE)
    one = models.PositiveIntegerField(default=0, null=True, blank=True)
    two = models.PositiveIntegerField(default=0, null=True, blank=True)
    three = models.PositiveIntegerField(default=0, null=True, blank=True)
    four = models.PositiveIntegerField(default=0, null=True, blank=True)
    five = models.PositiveIntegerField(default=0, null=True, blank=True)

    class Meta:
      ordering = ['artist']

    def __str__(self):
        # Extract all rating values and return max key.
        # Reverse this Dict if there is a tie and you want the last key.
        rating_list = {
          '1': self.one,
          '2': self.two,
          '3': self.three,
          '4': self.four,
          '5': self.five
        }
        return str(rating_list) + " " + self.artist.name
        #return str(max(rating_list, key=rating_list.get)) + " " + self.artist.name
  

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
