from django.db import models

class sales(models.Model):
    sid = models.CharField(max_length=20)
    sfirsttname = models.CharField(max_length=50)
    slastname = models.CharField(max_length=50)
    semail = models.EmailField()
    sphone = models.IntegerField(max_length=12)

class leads(models.Model):
    lname = models.CharField(max_length=50)
    lorganisation = models.CharField(max_length=50)
    lemail = models.EmailField()
    lphone = models.IntegerField(max_length=12)
    lsourceoflead = models.CharField(max_length=50)
   # lcreationdate = models.DateField()