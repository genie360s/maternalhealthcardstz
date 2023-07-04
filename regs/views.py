from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
# nida module
import pickle
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

def retrieve_mothers_card_information(request):
    mother = Patient.objects.select_related('pregnancy_info','mother_visit','lab_tests','clinical_attendance','mc_transmission').get(id=1)
    #mother = Patient.objects.get(id=1)
    print(mother.pregnancy_info)
    context = {
        'mother': mother

    }

    return render(request, 'regs/mothercard.html', context)

def retrieve_patients_in_the_hospital(request):
    patient_informations = Patient.objects.all()

    context = {
        'patient_informations': patient_informations

    }

    return render(request, 'regs/patients_database_view.html', context)

# preclampsia prediction 
def preclampsia_prediction(request):
    if request.method == 'POST':
        # Get the input data from the form submission
        feature1 = request.POST.get('feature1')
        feature2 = request.POST.get('feature2')
        # ... retrieve other input features

        # Load the trained model
        with open('random_forest_model.pkl', 'rb') as f:
            model = pickle.load(f)

        # Prepare the input data for prediction
        input_data = [[feature1, feature2, ...]]  # Create a 2D array with the input features

        # Make predictions using the loaded model
        predictions = model.predict(input_data)

        # Pass the predictions to the template for display
        context = {'predictions': predictions}
        return render(request, 'prediction/result.html', context)

    return render(request, 'prediction/predict.html')    