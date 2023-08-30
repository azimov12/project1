from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import MyModel, MyOffice
# Create your views here.

def all(request):
    result = []
    all_data = MyModel.objects.all()
    for user in all_data:
        result.append({
            'name': user.name,
            'phone': user.phone
        })
    return JsonResponse(result, safe=False)

def detail(request, my_id):
    a = MyModel.objects.get_object_or_404(id=my_id)
    data = {
        "name": a.name,
        'phone': a.phone
    }
    return JsonResponse(data, safe=False)

def all2(request):
    result = []
    all_data = MyOffice.objects.all()
    for user in all_data:
        result.append({
            'adress': user.adress,
            'email': user.email
        })
    return JsonResponse(result, safe=False)

def detail2(request, office_id):
    a = MyOffice.objects.get_object_or_404(id=office_id)
    data = {
            'adress': a.adress,
            'email': a.email
    }
    return JsonResponse(data, safe=False)