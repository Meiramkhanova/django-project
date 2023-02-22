from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return  HttpResponse('A page of people')

def categories(request):
    return HttpResponse("<h1>Page of a category</h1")