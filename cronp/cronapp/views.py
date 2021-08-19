from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
# Create your views here.


def index(request):

    return HttpResponse(datetime.now)




def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(index, 'interval', seconds=10)
    scheduler.start()