from django.db import models
from django.conf import settings


# Create your models here.

from django.contrib.auth.models import User


class User(User):
    national_id = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    
    # Additional fields for other user groups (researchers, hospitals, etc.) are be added here

# hospital model
class Hospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #additional fields specific to hospitals
    hospital_id = models.CharField(max_length=20, primary_key=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    hospital_type = models.CharField(max_length=50)
    affiliation = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    ward = models.CharField(max_length=50)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.user.email
    

# researcher model
class Researcher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #additional fields specific to researchers
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    institution_name = models.CharField(max_length=100)
    institution_id = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    res_national_id = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    agree_terms = models.BooleanField(default=False)
    

    def __str__(self):
        return self.user.email

# patient model
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # additional fields specific to patients
    regulator_id = models.CharField(max_length=20, unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    regulator_position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    national_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=150, unique=True)

    # Additional fields or methods can be added as needed

    def __str__(self):
        return self.username
    def __str__(self):
        return self.user.email
# regulator model
class Regulator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #additional fields specific to regulators
    regulator_id = models.CharField(max_length=20, unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    regulator_position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    national_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=150, unique=True)

    # Additional fields or methods can be added as needed

    def __str__(self):
        return self.username
    
    def __str__(self):
        return self.user.email

