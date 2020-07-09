from django.db import models

class Sales(models.Model):
    sid = models.CharField(max_length=20)
    sfirstname = models.CharField(max_length=50)
    slastname = models.CharField(max_length=50)
    semail = models.EmailField()
    sphone = models.IntegerField(max_length=12)

class Leads(models.Model):
    lname = models.CharField(max_length=50)
    lorganisation = models.CharField(max_length=50)
    lemail = models.EmailField()
    lphone = models.IntegerField(max_length=12)
    lsourceoflead = models.CharField(max_length=50)
