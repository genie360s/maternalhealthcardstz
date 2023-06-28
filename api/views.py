from django.shortcuts import render
import json  
from django.http import JsonResponse

# Create your views here.

def get_citizen_data(request, nida_number): # get_user_data , swapped with get_citizen_data

    with open('staticfiles/citizens/citizen.json') as file:
        users = json.load(file)
        for user in users:
            if user['nida_number'] == nida_number:
                return JsonResponse(user)
            print(user)

    return JsonResponse({'error': 'User not found.'}, status=404)

file_path = 'staticfiles/citizens/citizen.json'  # Provide the correct file path

def get_user_data(file_path, nida_number):
    with open(file_path) as file:
        users = json.load(file)
        for user in users:
            if user['nida_number'] == nida_number:
                return user

    return None