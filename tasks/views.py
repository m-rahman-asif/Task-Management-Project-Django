from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome")

def showTasks(request):
    return HttpResponse("These are  the tasks: ")

def showSpecificTask(request, id):
    return HttpResponse(f"This is specific task page {id}")