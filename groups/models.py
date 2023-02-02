from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
# Create your models here.

class HabitGroup(Group):
    title = models.CharField(max_length=100)
    members = models.ManyToManyField(User)