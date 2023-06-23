from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# nida module
from nida import load_user

from accounts.forms import PatientRegistrationForm
from accounts.views import login_required
from .models import Researcher, Patient, Hospital, Regulator

#rendering just pages

def index(request):
    return render(request, 'regs/index.html')

def register_research(request):
    if request.method == 'POST':
            print(request.POST)
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            institution_name = request.POST.get('institution_name')
            institution_id = request.POST.get('institution_id')
            phone_number = request.POST.get('phone_number')
            res_national_id = request.POST.get('res_national_id')
            email = request.POST.get('email')
            password = request.POST.get('password')
            agree_terms = request.POST.get('agree_terms')
            
            Researcher.objects.create(
                first_name=first_name,
                last_name=last_name,
                institution_name=institution_name,
                institution_id=institution_id,
                phone_number=phone_number,
                res_national_id=res_national_id,
                email=email,
                password=password,
                agree_terms=agree_terms
            )
            
            return redirect('regs/register_researcher.html')  # Assuming you have a URL pattern called 'success_page'
        
    return render(request, 'regs/register_researcher.html')

# patient views
def registeringpatient(request):
    return render(request, 'regs/dash_register_patient.html')

# main dashboard view
def dashboard(request):
    return render(request, 'regs/dashboard.html')

# research views
@login_required
def researchdashboard(request):
    return render(request, 'regs/researchdash.html')

def researchdashpublications(request):
    return render(request, 'regs/researchdash_publications.html')

def researchdashprofile(request):
    return render(request, 'regs/researchdash_profile.html')

# regulator views
def regulatordash(request):
    return render(request, 'regs/regulatordash.html')

def regulatordash_hospitals(request):
    return render(request, 'regs/regulatordash_hospitals.html')

def regulatordashprofile(request):
    return render(request, 'regs/regulatordashprofile.html')

def regulatordash_visualdata(request):
    return render(request, 'regs/regulatordash_visualdata.html')

def regulatordash_published(request):
    return render(request, 'regs/regulatordash_published.html')

def regulatordash_reports(request):
    return render(request, 'regs/regulatordash_reports.html')

def loader(request):
    return render(request, 'regs/loader.html')

# hospital dashboards
def hospitaldash(request):
    return render(request, 'regs/hospitaldash.html')

def hospitaldash_registerpatient(request):
    return render(request, 'regs/hospitaldash_registerpatient.html')

def hospitaldash_profile(request):
    return render(request, 'regs/hospitaldash_profile.html')

def hospitaldash_delivery(request):
    return render(request, 'regs/hospitaldash_delivery.html')

def hospitaldash_medicaldata(request):
    return render(request, 'regs/hospitaldash_medicaldata.html')


#function to load user details from nida

def retrieve_user(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        national_id = request.POST.get('nida_no')
        user_detail = load_user(national_id=national_id, json = True )
        print(user_detail)
        

        context = {
            'user_detail': user_detail
        }
        return render(request, 'regs/hospitaldash_registerpatient.html', context)
    else:
        return render(request, 'regs/hospitaldash_registerpatient.html')



       
def register_patient(request):

    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Creating a new Hospital instance and associating it with the user
            patient = Patient.objects.create(user=user)
            # Additional logic specific to hospitals
            
            login(request, user)
            return redirect('regs/retrieve_user')
    else:
        form = PatientRegistrationForm()
    return render(request, 'accounts/register_researcher.html', {'form': form})