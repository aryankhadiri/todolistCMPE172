# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from botocore.exceptions import ClientError
from django.shortcuts import render
import boto3
from boto3.dynamodb.conditions import Key, Attr
from datetime import date
from django.forms import formset_factory
from .forms import todoForm
import uuid
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):

    dynamodb = boto3.resource('dynamodb',region_name='us-west-1')
    tasks = dynamodb.Table("Tasks")
    taskDate = date.today().strftime('%Y-%m-%d')
    todoFormset = formset_factory(todoForm)
    if request.method == "POST" and request.POST.get("save")!=None:
        print(request.POST)
        forms = todoFormset(request.POST)
        if request.POST.get("date-input")!= '':
            taskDate = request.POST.get("date-input")        
            newForm = todoFormset(request.POST)
        date_items = getItem(tasks, request.user.id, taskDate)
        for item in date_items:
            checked = request.POST.get("done-"+str(item['id']))=='checked'
            deleted= request.POST.get("delete-"+str(item['id']))=='checked'
            #print(deleted)
            if (request.POST.get("done-"+str(item['id']))!= False):
                response = tasks.update_item(Key={
                    'id':item['id']
                },
                UpdateExpression='SET Done = :val1',
                ExpressionAttributeValues={
                ':val1': checked
                }
                )
            if (deleted):
                tasks.delete_item(Key={
                    'id':item['id']
                })
        #print(forms.errors)
        if int(request.POST.get('form-TOTAL_FORMS')) > 1:
            if forms.is_valid():
                print(forms)
                for form in forms[1:]:
                    unique_id = int((uuid.uuid1().int)/4)
                    data = form.cleaned_data
                    if data.get('task') != None:
                        tasks.put_item(Item={
                            'id':unique_id,
                        'Task': data.get('task'),
                        'userId':request.user.id,
                        'Task': data.get('task'),
                        'Done':data.get('done'),
                        'Date':taskDate
                        })
                    
    elif request.method == "POST" and request.POST.get("go-to-submit")!=None:
        taskDate = request.POST.get("date-input")
        date_items = getItem(tasks, request.user.id, taskDate)


            
    
    date_items = getItem(tasks, request.user.id, taskDate)
    context = {
        'tasks':date_items,
        'date': taskDate,
        'form':todoFormset
        #'forms': formset_factory
    }
    return render(request, 'home.html', context)
def getItem(table, Userid, date):
    try:
        response = table.scan(FilterExpression=Attr('userId').eq(Userid) & Attr('Date').eq(date))
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        if (response.get('Item')==False):
            return None
        else:
            return response['Items']