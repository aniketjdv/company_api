from django.db import models

# Create your models here.

class Company(models.Model):
    Company_types=[('IT','IT'),('Non IT','Non IT'),('GN','Genral')]
    comany_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=Company_types)
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self) :
        return self.name

class Employee(models.Model):
    emp_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    position=models.CharField(max_length=50,choices=[('MN','Manage'),('SD','Software Developer'),('HR','HR')])
    company=models.ForeignKey(Company,on_delete=models.CASCADE)  

    def __str__(self):
        return self.name