from django.db import models

# Create your models here.

class User(models.Model):
    GENDER_STATUS = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    VISITOR = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    last_bus_stop = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    visiting = models.CharField(max_length=100, choices=VISITOR, default='yes')    
    gender = models.CharField(max_length=20, choices=GENDER_STATUS, default='male')

class Admin(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username