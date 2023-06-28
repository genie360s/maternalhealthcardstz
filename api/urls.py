from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('users/<str:nida_number>/', views.get_user_data),
]
