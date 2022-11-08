from django.shortcuts import render
from django.http import HttpResponse
from project.AlgoAshutosh import *


# Create your views here.

def home(request):
    return HttpResponse("Hello I am here")


class backtest:
    def ironcondor(request):
        object = ironCondor() 
        object.ironCondorStrategy("datafiles/put-sample.csv","datafiles/call-sample(1).csv","datafiles/futures-sample.csv",100,100,200,200,1,10,50)
        
    def shorstraddle(request):
        object = shortStraddle()
        object.shortStraddleStrategy()
    
    def shortstrangle(request):
        object=shortStrangle()
        object.shortStrangleStrategy()
