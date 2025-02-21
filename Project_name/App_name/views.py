from django.shortcuts import render
import json

# first file of html link from main file 

def index(request):
    # create list for rendering into html files 
    # rendering is a method for render any file of html inside render methods we have to use first paremeter as request and another one is name of file of html
    #  
    return render(request,'index.html')



# about or who we are page 
def about(request):
    team_list = [
        {"Name" : "Akash Tiwari", "Dateofjoining" : "19/feb/2024", "Role" :"Developer & Trainer"},
        {"Name" : "Balram suryavanshi", "Dateofjoining" : "19/feb/2000", "Role" :"Senior Developer & Trainer"},
        {"Name" : "Anand Gupta", "Dateofjoining" : "19/feb/2004", "Role" :"Senior Developer & Trainer"},
        {"Name" : "Jay prakash pure", "Dateofjoining" : "19/feb/2002", "Role" :"Senior Developer & Trainer"},
        {"Name" : "Vilekh ", "Dateofjoining" : "19/feb/2001", "Role" :"Senior Developer & Trainer"},
        {"Name" : "Arpit gawasinde", "Dateofjoining" : "19/feb/2024", "Role" :"Developer & Trainer"},
        {"Name" : "Kashin malik", "Dateofjoining" : "19/feb/2024", "Role" :"Developer & Trainer"},
        {"Name" : "Sandeep Singh", "Dateofjoining" : "19/feb/2024", "Role" :"Developer & Trainer"},
        {"Name" : "Kapil tare", "Dateofjoining" : "19/feb/2024", "Role" :"Developer & Trainer"},
        {"Name" : "Piyush Pathak", "Dateofjoining" : "19/feb/2024", "Role" :"Developer & Trainer"},
        {"Name" : "Abhinav jain", "Dateofjoining" : "19/feb/2024", "Role" :"Developer & Trainer"},
        {"Name" : "Aasth jain", "Dateofjoining" : "19/feb/2024", "Role" :"Developer & Trainer"}
    ]
    return render(request, 'about.html', {'key': team_list})



# load json data 
import json
import os
from django.conf import settings
from django.http import JsonResponse

#load json data function 
def load_data(request):
    file_path = os.path.join(settings.BASE_DIR,'data.json') #absolute path
    if not os.path.exists(file_path):
        return JsonResponse("File not found",status = 404)
    
    with open(file_path,'r') as file:
        data = json.load(file)

        return JsonResponse({
            "message":"data loaded from json file", 'data': data
        },safe=False)
            
