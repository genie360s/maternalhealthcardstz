from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import HospitalRegistrationForm, ResearcherRegistrationForm, RegulatorRegistrationForm
from .models import Hospital ,Regulator , Researcher, Patient
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
            user = form.save(commit=False)
            user.save()
            # Creating a new researcher instance and associating it with the user
            researcher = Researcher.objects.create(
                user=user,
                institution_name=form.cleaned_data['institution_name'],
                institution_id=form.cleaned_data['institution_id'],
                phone_number=form.cleaned_data['phone_number'],
                national_id=form.cleaned_data['national_id'],
                email=form.cleaned_data['email'],
                password=user.password,  
                #agree_terms=form.cleaned_data['agree_terms']
            )
            return redirect('regs:research_dashboard')
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
            return redirect('hospital_dashboard')
    else:
        form = HospitalRegistrationForm()
    return render(request, 'accounts/hospital_register.html', {'form': form})

# forgot password
def forgot_password(request):
    return render(request, 'regs/forgot_password.html')

# login view for all users

def login_view(request):
    print(request.POST)
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(form.cleaned_data)
                  
            if user is not None:
                login(request, user)
                request.session['user_type'] = user.user_type
                if user.is_patient:
                    return redirect('regs:research_dashboard')
                elif user.is_hospital:
                    return redirect('regs:hospital_dashboard')
                elif user.is_regulator:
                    return redirect('regs:regulator_dashboard')
                elif user.is_researcher:
                    return redirect('regs:research_dashboard')
        else:
            print("not valid")
            print(form.errors)
    form = LoginForm()  # Creating an instance of the form

    return render(request, 'accounts/login.html', {'form': form})

# logout view

def logout_view(request):
    logout(request)
    return redirect('accounts:login')  # Replace 'home' with the URL or name of the desired redirect page after logout
