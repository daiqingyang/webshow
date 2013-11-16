from django.db import models
# Create your models here.
class AddClass(models.Model):
    className=models.CharField(max_length=20,unique=True)
    invate_key=models.CharField(max_length=30,unique=True)
    canRegister=models.BooleanField()
    def __unicode__(self):
        return self.className

class Student(models.Model):
    username=models.CharField(max_length=15,unique=True)
    password=models.CharField(max_length=10)
    className=models.CharField(max_length=20)
    invate_key=models.CharField(max_length=30)
    def __unicode__(self):
        return self.username
class Attendence(models.Model):
    username=models.CharField(max_length=15)
    className=models.CharField(max_length=20)
    date=models.DateField()
    time=models.TimeField()
    def __unicode__(self):
        return self.username
class Study_Day(models.Model):
    className=models.CharField(max_length=20)
    date=models.DateField()
    def __unicode__(self):
        return self.className,self.date
