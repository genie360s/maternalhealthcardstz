from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
# nida module
from nida import load_user
from django.contrib.auth.decorators import login_required
from accounts.forms import PatientRegistrationForm
from accounts.views import login_required
from accounts.models import Patient , User
from regs.models import PreviousPregnancyInformation
from regs.forms import ClinicalAttendanceForm, SpecialLaboratoryTestsForm, ObservationMotherFirstVisitForm, PreviousPregnanciesInformationForm, MotherChildTransmissionForm

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

# records medical data
def hospitaldash_medicaldata(request):
    form1 = ClinicalAttendanceForm()
    form2 = SpecialLaboratoryTestsForm()
    form3 = ObservationMotherFirstVisitForm()
    form4 = PreviousPregnanciesInformationForm()
    form5 = MotherChildTransmissionForm()
    if request.method == 'POST':
        form1 = ClinicalAttendanceForm(request.POST)
        form2 = SpecialLaboratoryTestsForm(request.POST)
        form3 = ObservationMotherFirstVisitForm(request.POST)
        form4 = PreviousPregnanciesInformationForm(request.POST)
        form5 = MotherChildTransmissionForm(request.POST)

        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            print("valid")
            form1.save()
            form2.save()
            form3.save()
            form4.save()
            form5.save()

            return redirect('accounts:successful_registered')
        else:
            print(form1.errors.as_json())
            print(form2.errors.as_json())
            print(form3.errors.as_json())
            print(form4.errors.as_json())
            print(form5.errors.as_json())
    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5
    }
    return render(request, 'regs/hospitaldash_medicaldata.html', context)


# retrieval of data

def retrieve_previous_pregancy_information(request):
    pregancy_information = PreviousPregnancyInformation.objects.all()
    

    context = {
        'pregancy_information': pregancy_information

    }

    return render(request, 'regs/mothercard.html', context)

def retrieve_patients_in_the_hospital(request):
    patient_informations = Patient.objects.all()

    context = {
        'patient_informations': patient_informations

    }

    return render(request, 'regs/patients_database_view.html', context)
