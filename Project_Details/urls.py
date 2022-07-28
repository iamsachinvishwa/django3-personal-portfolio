from django.urls import path
from .import views

app_name = 'Project_Details'

urlpatterns = [

    path('', views.projectdetails, name="projectdetails"),
]