from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date, datetime
import requests
# Create your views here.


def index(request):
    return HttpResponse(datetime.now())

def task_add():
    print('Executing', datetime.now())

def start():
    print('asdd')
    scheduler = BackgroundScheduler()
    scheduler.add_job(task_add, 'interval', seconds=10)
    scheduler.start()

# start()