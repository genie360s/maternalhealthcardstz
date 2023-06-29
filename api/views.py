from django.shortcuts import render
import json  
from datetime import datetime

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

#remember to swap if switch to the other fx to nida_no


def get_user_data(file_path, national_id):
    with open(file_path) as file:
        users = json.load(file)
        for user in users:
            if user['national_id'] == national_id:
                # Parse the date string and convert it to the desired format
                date_of_birth = datetime.strptime(user['date_of_birth'], "%d/%m/%Y").strftime("%Y-%m-%d")
                user['date_of_birth'] = date_of_birth
                return user
    return None