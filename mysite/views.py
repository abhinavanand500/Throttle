from django.shortcuts import render
from django.http import *
from .models import User, ActivityPeriod
from django.http import JsonResponse
# Create your views here.
def index(request):
    final_list=[]
    aa = {"ok" : "true"}
    keys_to_extract = ["start_time", "end_time"]
    values_db_user = User.objects.values()
    for users in values_db_user:
        team_a = users
        appending_array = []
        key=users['user_id']
        date_times = ActivityPeriod.objects.values()
        for dates in date_times:
            if(dates['user_id']==key):
                a_subset = {key : dates[key] for key in keys_to_extract}
                appending_array.append(a_subset)
        pem = {'activity_periods' : appending_array}
        mem = {**team_a,**pem}
        final_list.append(mem)
    last_dict = {'members':final_list}
    return JsonResponse({**aa,**last_dict})

def userdetails(request):
    params = User.objects.values()
    users=[]
    for i in params :
        users.append(i)
    return JsonResponse({"users": users})

def home(request):
    return HttpResponse("Your Server is ON. Use endpoints - ('getUserActDetails' to get all details of users and their time of starting and ending time) or use endpoint as 'getAllUsers' to get information of student.")

