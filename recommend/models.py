from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from djongo import models


# Create your models here.

class Movie(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    movie_logo = models.ImageField()

    def get_id(self):
        return self._id

    def __str__(self):
        return self.title


class Myrating(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

    def get_id(self):
        return self._id

class MyList(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watch = models.BooleanField(default=False)

    def get_id(self):
        return self._id
