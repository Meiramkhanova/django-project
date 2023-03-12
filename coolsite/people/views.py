from django.http import HttpResponse
from django.shortcuts import render
from .models import *

menu = [{'title': "ABOUT", 'url_name': 'about'},
        {'title': "ARTISTS", 'url_name': 'artists'},
        {'title': "AUDITION", 'url_name': 'audition'},
        {'title': "SIGN IN", 'url_name': 'login'}
]


def index(request):
    posts = People.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
    }
    return render(request, 'people/index.html', context=context)
def about(request):
    return render(request, 'people/index.html', {'menu': menu, 'title': 'О сайте'})
def artists(request):
    return HttpResponse("The page about artists")

def audition(request):
    return HttpResponse("The page about audition")
def login(request):
    return HttpResponse("Авторизация")
def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")
