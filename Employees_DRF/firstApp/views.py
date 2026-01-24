from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import emp

def employeeView(request):
    emp_ = {
        'id':1,
        'name':'Aranya',
        'salary':3698000
    }

    data = emp.objects.all()
    response = {'data':list(data.values('name','salary'))}
    return JsonResponse(response)
