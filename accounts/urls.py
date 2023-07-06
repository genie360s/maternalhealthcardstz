
from django.urls import path
from . import views
from .views import CustomPasswordResetConfirmView


# namespacing urls for easier url referencing
app_name = "accounts"


urlpatterns = [
    path("stakeholders", views.stakeholders, name="stakeholders"),
    # register urls
    path("register_hospital", views.register_hospital, name="register_hospital"),
    path("register_researcher", views.register_researcher, name="register_researcher"),
    path("register_regulator", views.register_regulator, name="register_regulator"),
    # patient registration
    path("hospital_registers_patient", views.hospital_registers_patient, name="hospital_registers_patient"),
    path("retrieve_user", views.retrieve_user, name="retrieve_user"),
    # general login
    path("login", views.login_view, name="login"),
    # general logout
    path('logout', views.logout_view, name="logout"),
    # generic sucess loader
    path('success', views.success_loader, name="success"),
    path('successful_registered', views.successful_registered, name="successful_registered"),
    path('successful_patient_registered', views.successful_patient_registered, name="successful_patient_registered"),
    path('card_success', views.card_success, name="card_success"),
    # password reset
    path("forgot_password", views.forgot_password, name="forgot_password"),
    path('successful_reset', views.successful_reset, name="successful_reset"),
    path('password_changed', views.successful_reset, name="password_changed"),
    path('password_reset', views.password_reset, name='password_reset'),
    path('password_update/<str:uidb64>/<str:token>/', CustomPasswordResetConfirmView.as_view(), name='password_update'),
   
 ]