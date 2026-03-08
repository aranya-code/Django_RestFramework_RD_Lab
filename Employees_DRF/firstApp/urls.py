from django.urls import path
from firstApp import views

# Creating a url path for employees list.
urlpatterns = [
    path('emp/', views.employeeView, name= 'employee_list'),
]