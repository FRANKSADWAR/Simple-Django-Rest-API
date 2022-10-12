from django.shortcuts import render
from django.http import JsonResponse
from drinkers.models import Drink
from drinkers.serializers import DrinkSerializer

def drink_list(request):
    # get all the drinks
    # serialize the drinks
    # return a JSON response
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse(serializer.data,safe=False)
