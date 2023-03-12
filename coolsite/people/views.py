from django.http import HttpResponse
from django.shortcuts import render
from .models import *

menu = ["ABOUT", "ARTISTS", "ACTORS", "SIGN IN", "AUDITION"]


def index(request):
    posts = People.objects.all()
    return render(request, 'people/index.html', {'posts': posts, 'menu': menu})


def about(request):
    return render(request, 'people/index.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def actress_page(request):
    return HttpResponse("The page about actress")  # i change add_page to actress


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")
