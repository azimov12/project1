from django.shortcuts import render, get_object_or_404
from .models import MyModel, MyOffice
from django.http import JsonResponse
from .serializers import MyModelSerializer, MyOfficeSerializer

# Create your views here.

def detail(request, my_id):
    m = get_object_or_404(MyModel, id = my_id)
    m_data = MyModelSerializer(m)
    
    return JsonResponse(m_data.data, safe=False)

def all(request):
    m = MyModel.objects.all()
    r = MyOfficeSerializer(m, many=True)
    
    return JsonResponse(r.data, safe=False)   


def detail2(request, office_id):
    offices = get_object_or_404(MyOffice, id = office_id)
    office_data = MyOfficeSerializer(offices)
    
    return JsonResponse(office_data.data, safe=False)

def all2(request):
    offices = MyOffice.objects.all()
    result = MyOfficeSerializer(offices, many=True)
    
    return JsonResponse(result.data, safe=False)      