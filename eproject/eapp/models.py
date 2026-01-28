from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Addregistration(models.Model):
    coursename=models.CharField(max_length=200,null=True,blank=True)
    mentorname=models.CharField(max_length=200,null=True,blank=True)
    coursefee=models.IntegerField(null=True,blank=True)
    courserating=models.FloatField(null=True,blank=True)
    coursedescription=models.CharField(max_length=500,null=True,blank=True)
    coursetype=models.CharField(max_length=50,null=True,blank=True)
    courseimage=models.ImageField(upload_to='courseimage',null=True,blank=True)
    def __str__(self):
        return self.coursename
