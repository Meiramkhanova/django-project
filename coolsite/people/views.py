from django.http import HttpResponse
from django.shortcuts import render

# Create your views
# here.
from .models import *
menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Actress", 'url_name': 'actress_page'},  #i change add_page to actress
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    posts = People.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
    }

    return render(request, 'people/index.html', context=context)
def about(request):
    return render(request, 'people/about.html', {'menu': menu,'title':'About a site'})

def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def actress_page(request):
    return HttpResponse("The page about actress")  #i change add_page to actress

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")
def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

