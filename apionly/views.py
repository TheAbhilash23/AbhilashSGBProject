from enum import auto
from functools import partial
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View


# from rest_framework import JSONResponse
from rest_framework.renderers import JSONRenderer
from SGBproject.models import Odb
from apionly.serializers import OdbSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io

# Create your views here.



def custid(request,pk):
    
    data = Odb.objects.get(custid=pk)
    
    serialdata = OdbSerializer(data)
    json_data = JSONRenderer().render(serialdata.data)
    
    return HttpResponse(json_data, content_type='application/json')
    
def showall(request):
    data = Odb.objects.all()
    serialdata = OdbSerializer(data,many=True)
    jsondata = JSONRenderer().render(serialdata.data)
    return HttpResponse(jsondata, content_type='application/json')



@csrf_exempt
def editdb(request):
    #For creating a new entry
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        
        python_data = JSONParser().parse(stream)  #JSONdata to Python datatype
        print(python_data)
        print(python_data.values())
        serializer = OdbSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Entry Created successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    

        
    #For editing an existing entry

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('custid')
        old = Odb.objects.get(custid=id)
        serializer = OdbSerializer(old,data = python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Entry Edited Successfully'}
            return JsonResponse(res)
        return JsonResponse(serializer.error)
    
    
    
    #For Deleting an existing entry
    
    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        
        print(pythondata)
        
        id = pythondata.get('custid')
        old = Odb.objects.get(custid=id)
        old.delete()
        
        res = {'msg':'Entry Deleted Successfully'}
        return JsonResponse(res)
            
        

    
@csrf_exempt
def analyzerapi(request):
    json_data = request.body
    stream = io.BytesIO(json_data)
    
    #Dependent variables extracted from the API as python data object
    pythondata = JSONParser().parse(stream)
    print('\n\n\npythonparsed data is\n\n\n',pythondata)
    #Values of Dependent variables stored as list (MUST BE IN ORDER OF ODB MODEL)
    #Importing basic libraries of data analysis.
    import pandas as pd
    
    X_predict = pd.DataFrame([pythondata])
    
    

    print(X_predict)
    print(type(X_predict))

    if LR is None:
        #Importing data from the database through models
        xinstance = Odb.objects.values('status',
                                    'duration',
                                    'credit_history',
                                    'purpose',
                                    'amount',
                                    'savings',
                                    'employment_duration',
                                    'installment_rate',
                                    'personal_status_sex',
                                    'other_debtors',
                                    'present_residence',
                                    'property_type',
                                    'age',
                                    'other_installment_plans',
                                    'housing',
                                    'number_credits',
                                    'job',
                                    'people_liable',
                                    'telephone',
                                    'foreign_worker')
        print('xinstance is as below\n\n\n', xinstance)
        yinstance = Odb.objects.filter().values('credit_risk')
        print('yinstance is as below \n\n', yinstance)

                

        
        xdf = pd.DataFrame(xinstance)
        ydf = pd.DataFrame(yinstance)
        
        #Importing train test split and logistic regression 
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LogisticRegression
        #Carrying out tts
        X_train, X_test, Y_train , Y_test = train_test_split(xdf,ydf,train_size=.75,stratify=ydf )
        print("Xtrain:\n",X_train.head(),"\nYtrain\n",Y_train)
        #Carrying out LogisticRegression on training dataset
        LR = LogisticRegression(random_state=0,solver='liblinear').fit(X_train, Y_train)
    prediction = LR.predict(X_predict)
    print('prediction is as below\n\n\n',prediction)
    
    pred = {'predict': prediction.astype(str)}
        
    return JsonResponse(pred)