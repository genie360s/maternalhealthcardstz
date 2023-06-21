
from django.urls import path

from . import views


# namespacing urls for easier url referencing
app_name = "accounts"

urlpatterns = [
    path("stakeholders", views.stakeholders, name="stakeholders"),
    path("login_patient", views.login_patient, name="login_patient"),   
    path("login_hospital", views.login_hospital, name="login_hospital"),
    path("register_hospital", views.register_hospital, name="register_hospital"),
    path("login_researcher", views.login_researcher, name="login_researcher"),
    path("register_researcher", views.register_researcher, name="register_researcher"),
    path("register_regulator", views.register_regulator, name="register_regulator"),
    path("login_regulator", views.login_regulator, name="login_regulator"),
    path("forgot_password", views.forgot_password, name="forgot_password"),

 ]