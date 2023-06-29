
from django.urls import path

from . import views


# namespacing urls for easier url referencing
app_name = "regs"

urlpatterns = [ 
    path("", views.index, name="home"),
    # generic dashboard ui
    path("dashboard", views.dashboard, name="dashboard"),
    # research dashboards
    path("research_dashboard", views.researchdashboard, name="research_dashboard"),
    path("researchdashpublications", views.researchdashpublications, name="researchdashpublications"),
    path("researchdashprofile", views.researchdashprofile, name="researchdashprofile"),
    # regulator dashboards
    path("regulator_dashboard", views.regulatordash, name="regulator_dashboard"),
    path("regulatordash_hospitals", views.regulatordash_hospitals, name="regulatordash_hospitals"),
    path("regulatordashprofile", views.regulatordashprofile, name="regulatordashprofile"),
    path("visualdata", views.regulatordash_visualdata, name="visualdata"),
    path("regulatordash_published", views.regulatordash_published, name="regulatordash_published"),
    path("regulatordash_reports", views.regulatordash_reports, name="regulatordash_reports"),
    # ui loader
    path("loader", views.loader, name="loader"),
    # hospital dashboards
    path("hospital_dashboard", views.hospitaldash, name="hospital_dashboard"),
    path("registerpatient", views.hospitaldash_registerpatient, name="registerpatient"),
    path("hospitaldashprofile", views.hospitaldash_profile, name="hospitaldashprofile"),
    path("hospitaldash_delivery", views.hospitaldash_delivery, name="hospitaldash_delivery"),
    path("hospitaldash_medicaldata", views.hospitaldash_medicaldata, name="hospitaldash_medicaldata"),
    path("register_patient", views.register_patient, name="register_patient")

]

