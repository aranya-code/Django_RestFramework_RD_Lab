from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import emp

def employeeView(request):
    # Fetch all employees data
    data = emp.objects.all()
    response = {'data':list(data.values('name','salary'))}
    return JsonResponse(response)
