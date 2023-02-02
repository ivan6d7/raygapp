from django.db import models
from django.contrib.auth.models import User
from groups.models import HabitGroup

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    creation_date = models.DateTimeField()
    group = models.ForeignKey(HabitGroup, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)