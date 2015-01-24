from django.db import models
from datetime import datetime

# Create your models here.

class Doctors(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    specialisation = models.CharField(max_length=200)

    def __unicode__(self):
        return self.firstname +" "+ self.lastname + " - " + self.specialisation

class Patients(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField()
    mobile = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now_add=True)
    appointmentdate = models.DateTimeField(null=False, blank=False, default=datetime.now())
    doctor = models.ForeignKey(Doctors)


    def __unicode__(self):
        return self.firstname +" "+ self.lastname





