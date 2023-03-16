from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import *

menu = [{'title': "ABOUT", 'url_name': 'about'},
        {'title': "ARTISTS", 'url_name': 'artists'},
        {'title': "AUDITION", 'url_name': 'audition'},
        {'title': "SIGN IN", 'url_name': 'login'}
]

def error_400(request, exception):
    # your custom error handling logic for Bad Request (400) error
    return render(request, '400.html', status=400)


def error_403(request, exception):
    # your custom error handling logic for Forbidden (403) error
    return render(request, '403.html', status=403)


def pageNotFound(request, exception):
    # your custom error handling logic for Not Found (404) error
    #return HttpResponseNotFound('<h1>Page Not Found</h1>')
    return render(request, '404.html', status=404)



def error_500(request):
    # your custom error handling logic for Internal Server Error (500) error
    return render(request, '500.html', status=500)


def check(request, exception):
    pass
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


def show_post(request, post_slug):
    post = get_object_or_404(People, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'people/post.html', context=context)
def show_category(request, cat_id):
    posts = People.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'people/index.html', context=context)
