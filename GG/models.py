from django.db import models
import datetime
import django.utils.timezone
from django.contrib.auth.models import User

# Create your models here.

#class for signup for user panel
class Signup(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    contact=models.CharField(max_length=15, null=True)
    role=models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.user.username

class Announce(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    adata=models.TextField(null=True)
    datime=models.DateTimeField()

    def __str__(self):
        return self.user.username

class Event(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    edate=models.CharField(max_length=15, null=True)
    etime=models.CharField(max_length=15, null=True)
    evenue=models.CharField(max_length=30, null=True)
    edata=models.TextField(null=True)
    eping=models.TextField(null=True)
    datime=models.DateTimeField()

    def __str__(self):
        return self.user.username        

class Feed(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fdata=models.TextField(null=True)
    fdatetime=models.DateTimeField()

    def __str__(self):
        return self.user.username