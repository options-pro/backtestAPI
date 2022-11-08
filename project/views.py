from django.shortcuts import render
from django.http import HttpResponse
from AlgoAshutosh import *


# Create your views here.

def home(request):
    return HttpResponse("Hello I am here")


def backtest(request):
    object = ironCondor() 
    object.ironCondorStrategy("put-sample.csv","call-sample(1).csv","futures-sample.csv",100,100,200,200,1,10,50)

    