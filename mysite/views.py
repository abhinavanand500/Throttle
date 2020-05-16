from django.shortcuts import render
from django.http import *
from .models import User, ActivityPeriod
from django.http import JsonResponse
# Create your views here.
def index(request):
    paa=[]
    aa = {"ok" : "true"}
    keys_to_extract = ["start_time", "end_time"]
    params = User.objects.values()
    for i in params:
        team_a = i
        d = []
        key=i['id1']
        dettimes = ActivityPeriod.objects.values()
        for j in dettimes:
            if(j['id1']==key):
                a_subset = {key : j[key] for key in keys_to_extract}
                d.append(a_subset)
        pem = {'activity_periods' : d}
        mem = {**team_a,**pem}
        paa.append(mem)
    para = {'members':paa}
    return JsonResponse({**aa,**para})
