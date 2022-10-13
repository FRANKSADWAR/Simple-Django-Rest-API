from symbol import pass_stmt
from django.shortcuts import render
from django.http import JsonResponse
from drinkers.models import Drink
from drinkers.serializers import DrinkSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status 
from rest_framework import schemas
from drf_yasg.utils import swagger_auto_schema







@swagger_auto_schema(method='POST',request_body=DrinkSerializer)
@swagger_auto_schema(method='GET')
@api_view(['GET','POST'])
def drink_list(request):

    # get all the drinks
    # serialize the drinks
    # return a JSON response

    ## The get view endpoint
    if request.method == "GET":
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    ## the post view endpoint
    if request.method == "POST":
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@swagger_auto_schema(method='get')
@swagger_auto_schema(method='put',request_body=DrinkSerializer)
@swagger_auto_schema(method='delete',request_body=DrinkSerializer)
@api_view(['GET','PUT','DELETE']) 
def drink_detail(request,id):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist :
        return Response(status= status.HTTP_404_NOT_FOUND)    
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)              
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
