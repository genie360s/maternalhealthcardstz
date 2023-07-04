from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
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

    regions = [
    'Arusha',
    'Dar es Salaam Region',
    'Dodoma',
    'Geita',
    'Iringa',
    'Kagera',
    'Kaskazini Pemba',
    'Kaskazini Unguja',
    'Katavi',
    'Kigoma',
    'Kilimanjaro',
    'Kusini Pemba',
    'Kusini Unguja',
    'Lindi',
    'Manyara',
    'Mara',
    'Mbeya',
    'Mjini Magharibi',
    'Morogoro',
    'Mtwara Region',
    'Mwanza',
    'Njombe',
    'Pwani Region',
    'Rukwa',
    'Ruvuma',
    'Shinyanga',
    'Simiyu',
    'Singida',
    'Tabora',
    'Tanga'
    ]

    REGION_CHOICES = [(region.lower().replace(' ', '_'), region) for region in regions]
    
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
    affiliation = forms.ChoiceField(
        label='Affiliation',
        choices=AFFILIATION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    region = forms.ChoiceField(
        label='Region',
        choices=REGION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select', 'required': True})
    )
    district = forms.CharField(
        label='District',
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': True})
    )
    ward = forms.CharField(
        label='Ward',
        widget=forms.TextInput(attrs={'class': 'form-control', 'required': True})
    )
    user_type = forms.ChoiceField(label='Register As', choices=User.USER_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-select'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email','phone_number']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            # 'hospital_name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'hospital_id': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

# researcher registration form
class ResearcherRegistrationForm(UserCreationForm):
    # adding additional fields specific to researchers
    institution_name = forms.CharField(label="Institution Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'University Of Dar es Salaam'}))
    institution_id = forms.IntegerField(label="Institution ID", widget=forms.NumberInput(attrs={'class': 'form-control', 'required': True}))
    agree_terms = forms.BooleanField(label="Agree to terms and conditions", widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id' : 'flexCheckChecked','value': 'True'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    user_type = forms.ChoiceField(label='Register As', choices=User.USER_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name','last_name','email', 'national_id', 'phone_number', 'user_type' ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'national_id': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'user_type': forms.Select(attrs={'class': 'form-select'}),
            
        }

# patient registration form
class PatientRegistrationForm(UserCreationForm):
    # adding additional fields specific to patients
    first_name = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    last_name = forms.CharField(label="Last Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    national_id = forms.CharField(label="National Id", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    phone_number = forms.CharField(label="Phone Number", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    email = forms.EmailField(label="Email", max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'required': True}))
    date_of_birth = forms.DateField(label="date of birth", widget=forms.DateInput(attrs={'class': 'form-control', 'required': True,'type': 'date'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [ 'first_name','last_name','national_id','phone_number','email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'national_id': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        
        }

# regulator registration form
class RegulatorRegistrationForm(UserCreationForm):
    # adding additional fields specific to  regulators
    first_name = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    last_name = forms.CharField(label="Last Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    phone_number = forms.CharField(label="Phone Number", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    regulator_position = forms.CharField(label="Regulator Position", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    user_type = forms.ChoiceField(label='Register As', choices=User.USER_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
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
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

# password reset form   
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address does not exist.")
        return email

#password set form
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm password'}))

