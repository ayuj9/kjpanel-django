from django.shortcuts import render
from .models import Names
from django.http import JsonResponse
import json

# Create your views here.


def index(request):
    return render(request , 'index.html')

# def get_names(request):
#     search = request.GET.get('search')
#     payload= []
#     if search:
#         objs = Names.objects.filter(name__startswith = search)

#         for obj in objs:
#             payload.append({
#              'name' : obj.name
#                })
     
#     return JsonResponse({
#           'status' : True , 
#           'payload' : payload  
#     })





def import_data(request):
    if request.method == 'POST' and request.FILES['json_file']:
        json_file = request.FILES['json_file']
        data = json.load(json_file)     
        for i in range(813,814):
            recipeLink = data[str(i)]['RecipieLink']
            recipeLink1 = data[str(i)]['RecipieLink_1']
            # print(i , recipeLnk1)
            # recipeL = recipeLink1
            if recipeLink == 'None':
                recipeL = recipeLink1
            else :
                recipeL = recipeLink    
            names = Names(

                id = data[str(i)]['ID'] , # Accessing data with str(i) as key
                name = data[str(i)]['Name'],
                recipieLink  = recipeL  # Adjust for correct key name
                
            )
            names.save()
        return render(request, 'index.html')
    return render(request, 'index.html')