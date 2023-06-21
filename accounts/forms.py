from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from .models import User

# user creation form

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# hospital registration form
class HospitalRegistrationForm(UserCreationForm):
    #choice tuples
    HOSPITAL_TYPE_CHOICES = [
        ('referral hospital', 'Referral Hospital'),
        ('regional hospital', 'Regional Hospital'),
        ('district hospital', 'District Hospital'),
        ('ward hospital', 'Ward Hospital'),
    ]

    AFFILIATION_CHOICES = [
        ('private hospital', 'Private'),
        ('religious hospital', 'Religious'),
        ('government hospital', 'Government'),
    ]
    
    hospital_name = forms.CharField(
        label='Hospital Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': True})
    )
    hospital_id = forms.CharField(
        label='Hospital ID',
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': True})
    )
    phone_number = forms.CharField(
        label='Phone Number',
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': True, 'type': 'tel'})
    )
    hospital_type = forms.ChoiceField(
        label='Hospital Type',
        choices=HOSPITAL_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    hospital_affiliation = forms.ChoiceField(
        label='Affiliation',
        choices=AFFILIATION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    hospital_region = forms.CharField(
        label='Region',
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': True})
    )
    hospital_district = forms.CharField(
        label='District',
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': True})
    )
    hospital_ward = forms.CharField(
        label='Ward',
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': True})
    )
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'phone_number']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            
        }

# researcher registration form
class ResearcherRegistrationForm(UserCreationForm):
    # adding additional fields specific to researchers
    first_name = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    last_name = forms.CharField(label="Second Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    institution_name = forms.CharField(label="Institution Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'University Of Dar es Salaam'}))
    institution_id = forms.IntegerField(label="Institution ID", widget=forms.NumberInput(attrs={'class': 'form-control', 'required': True}))
    agree_terms = forms.BooleanField(label="Agree to terms and conditions", widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'required': True}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'national_id', 'phone_number']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'national_id': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

# patient registration form
class PatientRegistrationForm(UserCreationForm):
    # adding additional fields specific to patients
    national_id = forms.CharField(label="national id", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [ 'national_id','phone_number']
        widgets = {

            'national_id': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        
        }

# regulator registration form
class RegulatorRegistrationForm(UserCreationForm):
    # adding additional fields specific to  regulators
    first_name = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    last_name = forms.CharField(label="Last Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    phone_number = forms.CharField(label="Phone Number", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm ', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm password'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [ 'first_name', 'last_name', 'national_id','phone_number', 'email' ]
        widgets = {

            'national_id': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

# loginform
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class ResetPasswordForm(PasswordResetForm):
    national_id = forms.CharField(max_length=40)

