
from django.urls import path

from . import views


# namespacing urls for easier url referencing
app_name = "regs"

urlpatterns = [ 
    path("", views.index, name="home"),

    path("dashboard", views.dashboard, name="dashboard"),
    path("researchdashboard", views.researchdashboard, name="researchdashboard"),
    path("researchdashpublications", views.researchdashpublications, name="researchdashpublications"),
    path("researchdashprofile", views.researchdashprofile, name="researchdashprofile"),
    path("regulatordash", views.regulatordash, name="regulatordash"),
    path("regulatordash_hospitals", views.regulatordash_hospitals, name="regulatordash_hospitals"),
    path("regulatordashprofile", views.regulatordashprofile, name="regulatordashprofile"),
    path("visualdata", views.regulatordash_visualdata, name="visualdata"),
    path("regulatordash_published", views.regulatordash_published, name="regulatordash_published"),
    path("regulatordash_reports", views.regulatordash_reports, name="regulatordash_reports"),
    path("loader", views.loader, name="loader"),
    path("hospitaldash", views.hospitaldash, name="hospitaldash"),
    path("registerpatient", views.hospitaldash_registerpatient, name="registerpatient"),
    path("hospitaldashprofile", views.hospitaldash_profile, name="hospitaldashprofile"),
    path("hospitaldash_delivery", views.hospitaldash_delivery, name="hospitaldash_delivery"),
    path("hospitaldash_medicaldata", views.hospitaldash_medicaldata, name="hospitaldash_medicaldata"),
    path("retrieve_user", views.retrieve_user, name="retrieve_user"),

]

