from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from countries.models import Countries
from countries.serializers import CountriesSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST'])  #decorator responsible for get and post request
def countries_list(request):  #view fn for getting and posting data
    if  request.method == 'GET':
        countries = Countries.objects.all()
        
        name = request.GET.get('name',None) #get name value
        if name is not  None:
            countries = countries.filter(name_icontains=name)
            #icontains checks if either the name or the description field contains the value of search _items. 
        countries_serializer = CountriesSerializer(countries,many=True) 
        #many=true is used for getting multiple data and serialize in order
        return JsonResponse(countries_serializer.data,safe=False)
    #'safe=false for objects serialization
    
    elif request.method == 'POST':
        countries_data = JSONParser().parse(request)
        countries_serializer = CountriesSerializer(data=countries_data) #stores the serialized data from the serializer class.
        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse(countries_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(countries_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['GET','PUT','DELETE'])
def countries_detail(request, pk):
    try:
        countries = Countries.objects.get(pk=pk)
    except Countries.DoesNotExit:
        return JsonResponse({'message': 'The country does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        countries_serializer = CountriesSerializer(countries)
        return JsonResponse(countries_serializer.data)
    
    elif request.method == 'PUT':
        countries_data = JSONParser().parser(request)
        countries_serializer = CountriesSerializer(countries, data=countries_data)
        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse(countries_serializer.data)
        return JsonResponse(countries_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        countries.delete()
        return JsonResponse({'message':'Country was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
        
        
        
        
        
        
        
        
        