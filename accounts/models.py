
from django.db import models
from django.conf import settings


# Create your models here.

from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    national_id = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    USER_TYPE_CHOICES = [
        ('P', 'Patient'),
        ('H', 'Hospital'),
        ('R', 'Regulator'),
        ('S', 'Researcher'),
    ]
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default='P')

    @property
    def is_patient(self):
        return self.user_type == 'P'

    @property
    def is_hospital(self):
        return self.user_type == 'H'

    @property
    def is_regulator(self):
        return self.user_type == 'R'

    @property
    def is_researcher(self):
        return self.user_type == 'S'
    class Meta:
        # prevents confusion with auth.User's reverse accessors
        swappable = 'AUTH_USER_MODEL'

    def save(self, *args, **kwargs):
        self.username = self.email  # Setting the username as the email
        super().save(*args, **kwargs)

    
# hospital model
class Hospital(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #additional fields specific to researchers
    institution_name = models.CharField(max_length=100)
    institution_id = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    national_id = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    agree_terms = models.BooleanField(default=False)
    

    def __str__(self):
        return self.user.email

# patient model
class Patient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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

