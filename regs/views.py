from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
# nida module
from nida import load_user
from django.contrib.auth.decorators import login_required
from accounts.forms import PatientRegistrationForm
from accounts.views import login_required
from .models import Researcher, Patient, Hospital, Regulator
import json
from api.views import get_user_data

#rendering just pages

def index(request):
    return render(request, 'regs/index.html')



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

# def retrieve_user(request):
#     if request.method == 'POST':
#         form = PatientRegistrationForm(request.POST)
#         national_id = request.POST.get('nida_no')
#         user_detail = load_user(national_id=national_id, json = True )
#         print(user_detail)
        

#         context = {
#             'user_detail': user_detail
#         }
#         return render(request, 'regs/hospitaldash_registerpatient.html', context)
#     else:
#         return render(request, 'regs/hospitaldash_registerpatient.html')


# def retrieve_user(request):
#     if request.method == 'POST':
#         nida_number = request.POST.get('nida_no')

#         with open('staticfiles/citizens/citizen.json') as file:
#             users = json.load(file)
#             for user in users:
#                 if user['nida_number'] == nida_number:
#                     user_detail = user
#                     print(user_detail)

#                     context = {
#                         'user_detail': user_detail
#                     }
#                     return render(request, 'regs/hospitaldash_registerpatient.html', context)

#         return JsonResponse({'error': 'User not found.'}, status=404)
#     else:
#         return render(request, 'regs/hospitaldash_registerpatient.html')

def retrieve_user(request):
    if request.method == 'POST':
        file_path = 'staticfiles/citizens/citizen.json'  # Provide the correct file path
        nida_number = request.POST.get('nida_no')
        user_detail = get_user_data(file_path, nida_number)

        if user_detail is not None:
            context = {
                'user_detail': user_detail
            }
            return render(request, 'regs/hospitaldash_registerpatient.html', context)

        return JsonResponse({'error': 'User not found.'}, status=404)
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