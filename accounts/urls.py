
from django.urls import path
from . import views
from .views import CustomPasswordResetConfirmView


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
    # general login
    path("login", views.login_view, name="login"),
    # general logout
    path('logout', views.logout_view, name="logout"),
    # generic sucess loader
    path('success', views.success_loader, name="success"),
    path('successful_registered', views.successful_registered, name="successful_registered"),
    path('successful_reset', views.successful_reset, name="successful_reset"),
    path('password_changed', views.successful_reset, name="password_changed"),
    path('password_reset', views.password_reset, name='password_reset'),
    path('password_update/<str:uid>/<str:token>/', CustomPasswordResetConfirmView.as_view(), name='password_update'),
   
 ]