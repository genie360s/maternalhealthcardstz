from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from sklearn.ensemble import RandomForestClassifier

# nida module
import pickle

import pandas as pd
from nida import load_user
from django.contrib.auth.decorators import login_required
from accounts.forms import PatientRegistrationForm
from accounts.views import login_required
from accounts.models import Patient, User
from regs.models import PreviousPregnancyInformation
from regs.forms import (
    ClinicalAttendanceForm,
    SpecialLaboratoryTestsForm,
    ObservationMotherFirstVisitForm,
    PreviousPregnanciesInformationForm,
    MotherChildTransmissionForm,
    PatientPredictorForm,
)
from django.db.models import Q

# rendering just pages


def index(request):
    return render(request, "regs/index.html")


# patient views
def registeringpatient(request):
    return render(request, "regs/dash_register_patient.html")


# main dashboard view
def dashboard(request):
    return render(request, "regs/dashboard.html")


# research views
@login_required
def researchdashboard(request):
    return render(request, "regs/researchdash.html")


def researchdashpublications(request):
    return render(request, "regs/researchdash_publications.html")


def researchdashprofile(request):
    return render(request, "regs/researchdash_profile.html")


# regulator views
def regulatordash(request):
    return render(request, "regs/regulatordash.html")


def regulatordash_hospitals(request):
    return render(request, "regs/regulatordash_hospitals.html")


def regulatordashprofile(request):
    return render(request, "regs/regulatordashprofile.html")


def regulatordash_visualdata(request):
    return render(request, "regs/regulatordash_visualdata.html")


def regulatordash_published(request):
    return render(request, "regs/regulatordash_published.html")


def regulatordash_reports(request):
    return render(request, "regs/regulatordash_reports.html")


def loader(request):
    return render(request, "regs/loader.html")


# hospital dashboards
def hospitaldash(request):
    return render(request, "regs/hospitaldash.html")


def hospitaldash_registerpatient(request):
    return render(request, "regs/hospitaldash_registerpatient.html")


def hospitaldash_profile(request):
    return render(request, "regs/hospitaldash_profile.html")


def hospitaldash_delivery(request):
    return render(request, "regs/hospitaldash_delivery.html")


# records medical data
def hospitaldash_medicaldata(request):
    form1 = ClinicalAttendanceForm()
    form2 = SpecialLaboratoryTestsForm()
    form3 = ObservationMotherFirstVisitForm()
    form4 = PreviousPregnanciesInformationForm()
    form5 = MotherChildTransmissionForm()

    # requesting session
    the_results = request.session.get("the_results")

    if request.method == "POST":
        form1 = ClinicalAttendanceForm(request.POST)
        form2 = SpecialLaboratoryTestsForm(request.POST)
        form3 = ObservationMotherFirstVisitForm(request.POST)
        form4 = PreviousPregnanciesInformationForm(request.POST)
        form5 = MotherChildTransmissionForm(request.POST)

        if (
            form1.is_valid()
            and form2.is_valid()
            and form3.is_valid()
            and form4.is_valid()
        ):
            print("valid")
            form1.save()
            form2.save()
            form3.save()
            form4.save()
            form5.save()

            return redirect("accounts:successful_registered")
        else:
            print(form1.errors.as_json())
            print(form2.errors.as_json())
            print(form3.errors.as_json())
            print(form4.errors.as_json())
            print(form5.errors.as_json())

    context = {
        "form1": form1,
        "form2": form2,
        "form3": form3,
        "form4": form4,
        "form5": form5,
        "the_results": the_results,
    }
    return render(request, "regs/hospitaldash_medicaldata.html", context)


# retrieval of data


def retrieve_mothers_card_information(request):
    mother = Patient.objects.select_related(
        "pregnancy_info",
        "mother_visit",
        "lab_tests",
        "clinical_attendance",
        "mc_transmission",
        "user",
    ).get(id=1)
    # mother = Patient.objects.get(id=1)
    context = {"mother": mother}

    return render(request, "regs/mothercard.html", context)


def retrieve_patients_in_the_hospital(request):
    patient_informations = Patient.objects.all()

    context = {"patient_informations": patient_informations}

    return render(request, "regs/patients_database_view.html", context)


# preclampsia prediction
def preclampsia_prediction(request):
    form = PatientPredictorForm()
    if request.method == "POST":
        # Get the input data from the form submission
        name = request.POST.get("patient_name")
        age = float(request.POST.get("age"))
        bmi = float(request.POST.get("bmi"))
        #weight = float(request.POST.get("weight"))
        diastolic_bp = float(request.POST.get("diastolic_bp"))
        systolic_bp = float(request.POST.get("systolic_bp"))
        history_of_hypertension = int(request.POST.get("history_of_hypertension"))
        proteinuria = int(request.POST.get("proteinuria"))
        family_history_of_preclampsia = int(request.POST.get("family_history"))

        print(name)
        # ... retrieve other input features

        # Load the trained model
        with open("staticfiles/model/random_forest_dmhcs_model.pkl", "rb") as f:
            rf = pickle.load(f)


        # Prepare the input data for prediction
        input_data = pd.DataFrame({
            'age': [age],
            'bmi': [bmi],
            'systolic_bp': [systolic_bp],
            'diastolic_bp': [diastolic_bp],
            'proteinuria': [proteinuria],
            'history_of_hypertension': [history_of_hypertension],
            'family_history_of_preclampsia': [family_history_of_preclampsia],
            
        })
        # Make predictions using the loaded model
        predictions = rf.predict(input_data)
        print(predictions)

        # Pass the predictions to the template for display
        context = {
            "predictions": predictions,
            "name": name
            }
        return render(request, "regs/ml-results.html", context)
    
    return render(request, "regs/ml-model-predictor.html", {"form": form})


# querrying patient


def search_patients(request):
    form1 = ClinicalAttendanceForm()
    form2 = SpecialLaboratoryTestsForm()
    form3 = ObservationMotherFirstVisitForm()
    form4 = PreviousPregnanciesInformationForm()
    form5 = MotherChildTransmissionForm()

    results = []
    if request.method == "POST":
        search_query = request.POST.get("search_patient")

        query = Patient.objects.filter(
            Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query)
        ).values("first_name", "last_name", "national_id")
        print(query)

        results = query
        # storing in a session
        the_results = list(results)
        request.session["results"] = the_results
        print(the_results)

    context = {
        "form1": form1,
        "form2": form2,
        "form3": form3,
        "form4": form4,
        "form5": form5,
        "results": results,
    }

    return render(request, "regs/hospitaldash_medicaldata.html", context)
