from django.db import models

# Create your models here.
class HydJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)

class BangaloreJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)

class MumbaiJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)


