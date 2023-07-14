from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse

# from accounts.models import User

# nida module
import pickle

import pandas as pd
from nida import load_user
from django.contrib.auth.decorators import login_required
from accounts.forms import PatientRegistrationForm
from accounts.views import login_required
from accounts.models import Hospital, Patient, User, Researcher
from regs.models import (
    PreviousPregnancyInformation,
    ResearchPublication,
    ResearchDataRequest,
    MotherFirstVisit,
    SpecialLaboratoryTests,
    ClinicalAttendance,
    MotherChildTransmission,
)

from regs.forms import (
    ClinicalAttendanceForm,
    SpecialLaboratoryTestsForm,
    ObservationMotherFirstVisitForm,
    PreviousPregnanciesInformationForm,
    MotherChildTransmissionForm,
    PatientPredictorForm,
    ResearchPublicationForm,
    DataRequestForm,
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
    national_id = request.user.national_id
    researcher = get_object_or_404(Researcher, national_id=national_id)
    publications = ResearchPublication.objects.filter(res_national_id=researcher)
    data_requests = ResearchDataRequest.objects.filter(res_national_id=researcher)
    # Get the number of publications
    publication_count = ResearchPublication.objects.filter(res_national_id=researcher).count()
    
    # Get the number of data requests
    data_request_count = ResearchDataRequest.objects.filter(res_national_id=researcher).count()

    print(publications)
    print(data_requests)

    context = {
        "publications": publications,
        "data_requests": data_requests,
        "publication_count" : publication_count,
        "data_request_count" : data_request_count,
    }

    return render(request, "regs/researchdash.html", context)


@login_required
def researchdashpublications(request):
    national_id = request.user.national_id
    researcher = get_object_or_404(Researcher, national_id=national_id)
    publications = ResearchPublication.objects.filter(res_national_id=researcher)
    data_requests = ResearchDataRequest.objects.filter(res_national_id=researcher)

    # Get the number of publications
    publication_count = ResearchPublication.objects.filter(res_national_id=researcher).count()
    
    # Get the number of data requests
    data_request_count = ResearchDataRequest.objects.filter(res_national_id=researcher).count()

    print(publications)
    print(data_requests)
    print(publication_count)
    print(data_request_count)

    # Rendering instance forms
    research_form = ResearchPublicationForm()
    data_request_form = DataRequestForm()

    if request.method == "POST":
        if "research_form_submit" in request.POST:
            research_form = ResearchPublicationForm(request.POST, request.FILES)
            if research_form.is_valid():
                research_form.instance.res_national_id = researcher
                print("Research form is valid")
                research_form.save()
                return redirect("accounts:publish_success")
            else:
                print(research_form.errors.as_json())

        elif "data_request_form_submit" in request.POST:
            data_request_form = DataRequestForm(request.POST, request.FILES)
            if data_request_form.is_valid():
                print("Data Request form is valid")
                data_request_form.save()
                return redirect("accounts:data_request_success")
            else:
                print(data_request_form.errors.as_json())

    context = {
        "research_form": research_form,
        "data_request_form": data_request_form,
        "publications": publications,
        "data_requests": data_requests,
        "publication_count": publication_count,
        "data_request_count": data_request_count,
    }

    return render(request, "regs/researchdash_publications.html", context)


@login_required
def researchdashprofile(request):
    return render(request, "regs/researchdash_profile.html")


# regulator views
@login_required
def regulatordash(request):
    publications = ResearchPublication.objects.all()
    data_requests = ResearchDataRequest.objects.all()
    # Get the number of publications
    publication_count = ResearchPublication.objects.count()  
    print(publication_count)
    hospital_count = Hospital.objects.count()  
    patient_count = Patient.objects.count()
    # Get the number of data requests
    data_request_count = ResearchDataRequest.objects.count()

    context = {
        "publications": publications,
        "data_requests": data_requests,
        "publication_count" : publication_count,
        "data_request_count" : data_request_count,
        "hospital_count" : hospital_count,
        "patient_count" : patient_count,
    }

    return render(request, "regs/regulatordash.html", context)


@login_required
def regulatordash_hospitals(request):
    return render(request, "regs/regulatordash_hospitals.html")


@login_required
def regulatordashprofile(request):
    return render(request, "regs/regulatordashprofile.html")


@login_required
def regulatordash_visualdata(request):
    return render(request, "regs/regulatordash_visualdata.html")


@login_required
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
@login_required
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

            return redirect("accounts:card_success")
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


# has some issues to work on

def retrieve_mothers_card_information(request):
    mother = Patient.objects.select_related(
        "pregnancy_info",
        "mother_visit",
        "lab_tests",
        "clinical_attendance",
        "mc_transmission",
        "user",
    ).get(id=2)
    # mother = Patient.objects.get(id=1)
    context = {"mother": mother}

    return render(request, "regs/mothercard.html", context)

@login_required
def retrieve_patients_in_the_hospital(request):
    patients = Patient.objects.all()
    patient_data = []

    for patient in patients:
        pre_preg_infos = PreviousPregnancyInformation.objects.filter(patient=patient)
        mother_visits = MotherFirstVisit.objects.filter(patient=patient)
        lab_tests = SpecialLaboratoryTests.objects.filter(patient=patient)
        clinical_attendances = ClinicalAttendance.objects.filter(patient=patient)
        mc_transmissions = MotherChildTransmission.objects.filter(patient=patient)

        patient_data.append(
            {
                "patient": patient,
                "pre_preg_infos": pre_preg_infos,
                "mother_visits": mother_visits,
                "lab_tests": lab_tests,
                "clinical_attendances": clinical_attendances,
                "mc_transmissions": mc_transmissions,
            }
        )

    context = {
        "patient_data": patient_data,
        "patients": patients,
    }

    return render(request, "regs/patients_database_view.html", context)


# preclampsia prediction
@login_required
def preclampsia_prediction(request):
    form = PatientPredictorForm()
    if request.method == "POST":
        # Get the input data from the form submission
        name = request.POST.get("patient_name")
        age = float(request.POST.get("age"))
        bmi = float(request.POST.get("bmi"))
        # weight = float(request.POST.get("weight"))
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
        input_data = pd.DataFrame(
            {
                "age": [age],
                "bmi": [bmi],
                "systolic_bp": [systolic_bp],
                "diastolic_bp": [diastolic_bp],
                "proteinuria": [proteinuria],
                "history_of_hypertension": [history_of_hypertension],
                "family_history_of_preclampsia": [family_history_of_preclampsia],
            }
        )
        # Make predictions using the loaded model
        predictions = rf.predict(input_data)
        print(predictions)

        # Pass the predictions to the template for display
        context = {"predictions": predictions, "name": name}
        return render(request, "regs/ml-results.html", context)

    return render(request, "regs/ml-model-predictor.html", {"form": form})


# querrying patient

@login_required
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

@login_required
def patient_track(request, national_id):
    patient = Patient.objects.get(national_id=national_id)
    print(patient)

    
    pre_preg_infos = PreviousPregnancyInformation.objects.filter(patient=patient)
    mother_visits = MotherFirstVisit.objects.filter(patient=patient)
    lab_tests = SpecialLaboratoryTests.objects.filter(patient=patient)
    clinical_attendances = ClinicalAttendance.objects.filter(patient=patient)
    mc_transmissions = MotherChildTransmission.objects.filter(patient=patient)

    patient_data = []

    patient_data.append(
        {
            "patient": patient,
            "pre_preg_infos": pre_preg_infos,
            "mother_visits": mother_visits,
            "lab_tests": lab_tests,
            "clinical_attendances": clinical_attendances,
            "mc_transmissions": mc_transmissions,
        }
    )

    print(patient_data)
    
    context = {
        "patient": patient,
        "patient_data": patient_data,
    }
    return render(request, "regs/patient_track.html", context)


@login_required
def patient_graph(request, national_id):
    patient = Patient.objects.get(national_id=national_id)
    print(patient)

    
    pre_preg_infos = PreviousPregnancyInformation.objects.filter(patient=patient)
    mother_visits = MotherFirstVisit.objects.filter(patient=patient)
    lab_tests = SpecialLaboratoryTests.objects.filter(patient=patient)
    clinical_attendances = ClinicalAttendance.objects.filter(patient=patient)
    mc_transmissions = MotherChildTransmission.objects.filter(patient=patient)
    total_weight = sum(attendance.weight for attendance in clinical_attendances)
    patient_data = []

    patient_data.append(
        {
            "patient": patient,
            "pre_preg_infos": pre_preg_infos,
            "mother_visits": mother_visits,
            "lab_tests": lab_tests,
            "clinical_attendances": clinical_attendances,
            "mc_transmissions": mc_transmissions,
            
        }
    )

    # print(patient_data)
    print(total_weight)
    
    context = {
        "patient": patient,
        "patient_data": patient_data,
        "total_weight": total_weight,
    }
    return render(request, "regs/patient_graph.html", context)