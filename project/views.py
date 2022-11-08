from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from project.AlgoAshutosh import *
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

def home(request):
    return HttpResponse("Hello I am here")


class backtest:
    putFile="datafiles/put-sample.csv"
    callFile="datafiles/call-sample(1).csv"
    spotFile="datafiles/futures-sample.csv"

    @csrf_exempt
    def ironcondor(self,request):
        
        if request.method=='POST':
            sellPut=request.POST.get('sellPut')
            sellCall=request.POST.get('sellCall')
            buyCall=request.POST.get('buyCall')
            buyPut=request.POST.get('buyPut')
            entry=request.POST.get('entry')
            exit=request.POST.get('exit')
            lotSize=request.POST.get('lotSize')        
            object = ironCondor() 
            profit=object.ironCondorStrategy(self.putFile,self.callFile,self.spotFile,sellPut,sellCall,buyCall,buyPut,entry,exit,lotSize)
            jsonr=json.dumps(profit)
            return JsonResponse(jsonr,safe=False)
        elif request.method=="GET":
            return HttpResponse("Error Happened")
        

    def shorstraddle(self,request):        
        entry=request.POST.get('entry')
        exit=request.POST.get('exit')
        lotSize=request.POST.get('lotSize')
        object = shortStraddle()
        profit=object.shortStraddleStrategy(self.putFile,self.callFile,self.spotFile,entry,exit,lotSize)
        jsonr=json.dumps(profit)
        return JsonResponse(jsonr,safe=False)
    
    def shortstrangle(self,request):
        sellPut=request.POST.get('sellPut')
        sellCall=request.POST.get('sellCall')
        entry=request.POST.get('entry')
        exit=request.POST.get('exit')
        lotSize=request.POST.get('lotSize')
        object=shortStrangle()
        profit=object.shortStrangleStrategy(self.putFile,self.callFile,self.spotFile,sellPut,sellCall,entry,exit,lotSize)
        jsonr=json.dumps(profit)
        return JsonResponse(jsonr,safe=False)
    
    def test(self,request):
        return HttpResponse("Hello from test")
