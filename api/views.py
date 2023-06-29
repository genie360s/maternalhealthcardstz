from django.shortcuts import render
import json  
from django.http import JsonResponse

# Create your views here.

def get_citizen_data(request, national_id): # get_user_data , swapped with get_citizen_data

    with open('staticfiles/citizens/citizen.json') as file:
        users = json.load(file)
        for user in users:
            if user['national_id'] == national_id:
                return JsonResponse(user)
            print(user)

    return JsonResponse({'error': 'User not found.'}, status=404)

file_path = 'staticfiles/citizens/citizen.json'  # Provide the correct file path

def get_user_data(file_path, national_id): # remember to swap if switch to the other fx to nida_no
    with open(file_path) as file:
        users = json.load(file)
        for user in users:
            if user['national_id'] == national_id:
                return user

    return None