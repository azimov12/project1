from django.shortcuts import render, get_object_or_404
from .models import MyModel, MyOffice
from django.http import JsonResponse
from .serializers import MyModelSerializer, MyOfficeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class Detail(APIView):
    def get(self, request, *args, **kwargs):
        m = get_object_or_404(MyModel, id = kwargs['my_id'])
        res = MyModelSerializer(m)
        return Response(res.data)

class All(APIView):    
    def get(self, request):
        model = MyModel.objects.all()
        result = MyModelSerializer(model, many=True)
        
        return Response(result.data)   


class Detail2(APIView):
    def get(self, request, *args, **kwargs):
        office = get_object_or_404(MyOffice, id = kwargs['my_office__id'])
        result = MyOfficeSerializer(office)

        return Response(result.data)

class All2(APIView):
    def get(self, request):
        office = MyOffice.objects.all()
        res = MyOfficeSerializer(office, many=True)

        return Response(res.data)   

class CreateModelView(APIView):
    def post(self, request):
        user_body = request.data 
        serializer = MyModelSerializer(data = user_body)          
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)    

class CreateOfficeView(APIView):
    def post(self, request):
        body = request.data 
        s = MyOfficeSerializer(data = body)          
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors) 