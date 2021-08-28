from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date, datetime
import requests
from django.shortcuts import redirect
# Create your views here.


def index(request):
    print("view")
    return HttpResponse(datetime.now())

def task_add():
    f'curl -X GET "http://127.0.0.1:8000/"'
    print('Executing', datetime.now())
  

def start():
    print('asdd')
    scheduler = BackgroundScheduler()
    scheduler.add_job(task_add, 'interval', seconds=10)
    scheduler.start()

    