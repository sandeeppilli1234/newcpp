from django.db import models

# Create your models here.

class login(models.Model):
    username= models.CharField(null=False,max_length= 20)
    password = models.CharField(null=False, max_length=20)
    cust_id = models.ForeignKey("Registered",on_delete=models.CASCADE)

class Registered(models.Model):
    email= models.CharField(null=True,max_length=100)
    firstname= models.CharField(null=True,max_length=100)
    lastname= models.CharField(null=True,max_length=100)
    username = models.CharField(null=True,max_length=100)
    password = models.CharField(null=True,max_length=100)
    
class Enquiries(models.Model):
    enquirer_name = models.CharField(null=True,max_length=100)
    enquirer_email = models.CharField(null=True,max_length=100)
    enquiry_msg =models.CharField(null=True,max_length=100)

class Property(models.Model):
    hoster =models.CharField(null=True,max_length=100)
    Name_Address = models.CharField(null=True,max_length=100)
    segment = models.CharField(null=True,max_length=100)
    price = models.CharField(null=True,max_length=100)
    Area = models.CharField(null=True,max_length=100)
    Status = models.CharField(null=True,max_length=100)

