from django.shortcuts import render
import json  
from django.http import JsonResponse

# Create your views here.

def get_user_data(request, nida_number):

    with open('staticfiles/citizen/citizen.json') as file:
        users = json.load(file)
        for user in users:
            if user['nida_number'] == nida_number:
                return JsonResponse(user)
            print(user)

    return JsonResponse({'error': 'User not found.'}, status=404)