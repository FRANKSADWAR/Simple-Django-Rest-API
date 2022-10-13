from django.shortcuts import render
from django.http import JsonResponse
from drinkers.models import Drink
from drinkers.serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 

from drinks import drinkers

@api_view(['GET','POST'])
def drink_list(request):

    # get all the drinks
    # serialize the drinks
    # return a JSON response

    ## The get view endpoint
    if request.method == "GET":
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse({'drinks':serializer.data})

    ## the post view endpoint
    if request.method == "POST":
        pass
 
def drink_view(request,id):
    pass