from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from project.AlgoAshutosh import *
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

def home(request):
    # id=int(request.GET.get('id')
    # print("id=============",id)
    return HttpResponse("Hello I am here",id)


class backtest:
    putFile="datafiles/put-sample.csv"
    callFile="datafiles/call-sample(1).csv"
    spotFile="datafiles/futures-sample.csv"

    @csrf_exempt
    
    def ironcondor(self,request):
        print(request.GET)
        
        if request.method=='GET':
            sellPut=int(request.GET.get('sellPut'))
            sellCall=int(request.GET.get('sellCall'))
            buyCall=int(request.GET.get('buyCall'))
            buyPut=int(request.GET.get('buyPut'))
            entry=int(request.GET.get('entry'))
            exit=int(request.GET.get('exit'))
            lotSize=int(request.GET.get('lotSize'))   
            print(str(sellCall)+" *******************")     
            object = ironCondor() 
            profit=object.ironCondorStrategy(self.putFile,self.callFile,self.spotFile,sellPut,sellCall,buyCall,buyPut,entry,exit,lotSize)
            jsonr=json.dumps(profit)
            jsonr=json.loads(jsonr)
            return JsonResponse(jsonr,safe=False)
        elif request.method=="POST":
            return HttpResponse("Error Happened")
        

    def shorstraddle(self,request):        
        entry=int(request.GET.get('entry'))
        exit=int(request.GET.get('exit'))
        lotSize=int(request.GET.get('lotSize'))
        object = shortStraddle()
        profit=object.shortStraddleStrategy(self.putFile,self.callFile,self.spotFile,entry,exit,lotSize)
        jsonr=json.dumps(profit)
        jsonr=json.loads(jsonr)
        return JsonResponse(jsonr,safe=False)
    
    def shortstrangle(self,request):
        sellPut=int(request.GET.get('sellPut'))
        sellCall=int(request.GET.get('sellCall'))
        entry=int(request.GET.get('entry'))
        exit=int(request.GET.get('exit'))
        lotSize=int(request.GET.get('lotSize'))
        object=shortStrangle()
        profit=object.shortStrangleStrategy(self.putFile,self.callFile,self.spotFile,sellPut,sellCall,entry,exit,lotSize)
        jsonr=json.dumps(profit)
        jsonr=json.loads(jsonr)
        return JsonResponse(jsonr,safe=False)
    
    def test(self,request):
        return HttpResponse("Hello from test")
