from django.shortcuts import render
from django.contrib.auth import authenticate, login
from accounts.forms import HospitalRegistrationForm, ResearcherRegistrationForm, RegulatorRegistrationForm
from .models import Hospital ,Regulator
from .forms import LoginForm 
# Create your views here.

# stakeholders views
def stakeholders(request):
    return render(request, 'accounts/stakeholders.html')

# patient views
def login_patient(request):
    return render(request, 'accounts/login_patient.html')

# regulator views
def register_regulator(request):
    if request.method == 'POST':
        form = RegulatorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Creating a new Hospital instance and associating it with the user
            regulator = Regulator.objects.create(user=user)
            # Additional logic specific to hospitals
            
            login(request, user)
            return redirect('accounts/researchdashboard')
    else:
        form = RegulatorRegistrationForm()
    return render(request, 'accounts/register_regulator.html', {'form': form})

def login_regulator(request):
    return render(request, 'accounts/login_regulator.html')

# researcher views
def login_researcher(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'accounts/login_researcher.html')

def register_researcher(request):

    if request.method == 'POST':
        form = ResearcherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Creating a new Hospital instance and associating it with the user
            hospital = Hospital.objects.create(user=user)
            # Additional logic specific to hospitals
            
            login(request, user)
            return redirect('accounts/researchdashboard')
    else:
        form = ResearcherRegistrationForm()
    return render(request, 'accounts/register_researcher.html', {'form': form})

# hospital views
def login_hospital(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None and user.is_hospital:
                login(request, user)
                return redirect('hospital_dashboard')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = LoginForm()

    return render(request, 'hospital_login.html', {'form': form})



def register_hospital(request):
    if request.method == 'POST':
        form = HospitalRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Creating a new Hospital instance and associating it with the user
            hospital = Hospital.objects.create(user=user)
            # Additional logic specific to hospitals
            
            login(request, user)
            return redirect('hospitaldash')
    else:
        form = HospitalRegistrationForm()
    return render(request, 'accounts/hospital_register.html', {'form': form})

# forgot password
def forgot_password(request):
    return render(request, 'regs/forgot_password.html')

# authentication views

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
# from .forms import RegistrationForm, LoginForm, ResetPasswordForm

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return redirect('login')
#     else:
#         form = RegistrationForm()
#     return render(request, 'accounts/register.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request, data=request.POST)
#         if form.is_valid():
#             national_id = form.cleaned_data['national_id']
#             email = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('dashboard')  # Replace with the desired URL after login
#     else:
#         form = LoginForm()
#     return render(request, 'accounts/login.html', {'form': form})

# def user_logout(request):
#     logout(request)
#     return redirect('login')  # Replace with the desired URL after logout
