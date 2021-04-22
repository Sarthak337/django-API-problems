from django.shortcuts import render
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from tutorials.models import Tutorial,Bookings
from tutorials.serializers import TutorialSerializer,BookingSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view

@api_view(['GET', 'PUT', 'POST'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try: 
        tutorial = Tutorial.objects.get(pk=pk)
    except Tutorial.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = TutorialSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 

@api_view(['GET', 'PUT', 'DELETE'])
def booking_list(request, pk):
    try: 
        book = Bookings.objects.get(pk=pk) 
    except Tutorial.DoesNotExist: 
        return JsonResponse({'message': 'The booking does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        bookings_serializer = BookingSerializer(book) 
        return JsonResponse(bookings_serializer.data) 
 
    elif request.method == 'PUT': 
        book_data = JSONParser().parse(request) 
        bookings_serializer = BookingSerializer(book_data, data=book_data) 
        if bookings_serializer.is_valid(): 
            bookings_serializer.save() 
            return JsonResponse(bookings_serializer.data) 
        return JsonResponse(bookings_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 


    