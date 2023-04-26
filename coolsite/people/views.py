from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .forms import *
from .models import *
from .serializers import PeopleSerializer
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics, viewsets, mixins


class PeopleHome(DataMixin, ListView):
    model = People
    template_name = 'people/index.html'
    context_object_name = 'posts'  # we can not write here menu, due to reason that it is dynamic

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main Page")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):  # to make a choice in panel admin to publish or not
        return People.objects.filter(is_published=True).select_related('cat')


# def index(request):
#   posts = People.objects.all()
#  context = {
#     'posts': posts,
#    'menu': menu,
# }
# return render(request, 'people/index.html', context=context)

def audition_people(request):
    posts = Audition.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
    }
    return render(request, 'people/audition_people.html', context=context)


@login_required
def about(request):
    contact_list = People.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer, display the first page.
        page_obj = paginator.get_page(1)
    except EmptyPage:
        # If page_number is out of range, display the last page of results.
        page_obj = paginator.get_page(paginator.num_pages)

    return render(request, 'people/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'О сайте'})


def artists(request):
    return HttpResponse("The page about artists")


class AddInfo(LoginRequiredMixin, DataMixin, CreateView):
    login_url = reverse_lazy('home')
    raise_exception = True
    form_class = AddPostForm
    template_name = 'people/addinfo.html'
    success_url = reverse_lazy('audition_people')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Add An Information'
        # context['menu'] = menu
        # return context
        c_def = self.get_user_context(title="Добавление статьи")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


# def audition(request):
# if request.method == 'POST':
# form = AddPostForm(request.POST,request.FILES)
# if form.is_valid():
# form.save()
# return redirect('audition_people')
# else:
# form = AddPostForm()
# return render(request, 'people/addinfo.html', {'menu': menu, 'title': 'Добавление статьи', 'form': form})


# def login(request):
#     return HttpResponse("Авторизация")


class ShowPost(DataMixin, DetailView):
    model = People
    template_name = 'people/post.html'
    slug_url_kwarg = 'post_slug'
    # pk_url_kwarg = 'post_pk'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


# def show_post(request, post_slug):
# post = get_object_or_404(People, slug=post_slug)

# context = {
# 'post': post,
# 'menu': menu,
# 'title': post.title,
# 'cat_selected': post.cat_id,
# }

# return render(request, 'people/post.html', context=context)


class PeopleCategory(DataMixin, ListView):
    paginate_by = 3
    model = People
    template_name = 'people/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        return People.objects.filter(cat_slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)

        return dict(list(context.items()) + list(c_def.items()))


# def show_category(request, cat_id):
# posts = People.objects.filter(cat_id=cat_id)

# if len(posts) == 0:
# raise Http404()

# context = {
# 'posts': posts,
# 'menu': menu,
# 'title': 'Отображение по рубрикам',
# 'cat_selected': cat_id,
# }

# return render(request, 'people/index.html', context=context)

def audition_all(request):
    context = {
        'menu': menu,
    }
    return render(request, 'people/audition.html', context=context)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'people/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Registration")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'people/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Authorization")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'people/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Feedback")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class PeopleViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    # queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return People.objects.all()[:4]

        return People.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk= None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

# class PeopleAPIList(generics.ListCreateAPIView):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer
#
#
# class PeopleAPIUpdate(generics.UpdateAPIView):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer
#
#
# class PeopleAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer


# class PeopleAPIView(APIView):
#     def get(self,request):
#         p = People.objects.all()
#         return Response({'posts': PeopleSerializer(p, many=True).data})
#
#     def post(self, request):
#         serializer = PeopleSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self,request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = People.objects.get(pk = pk)
#
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = PeopleSerializer(data=request.data, instance = instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#
# if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             instance = People.objects.get(pk = pk)
#             instance.delete()
#
#         except :
#             return Response({"error" : "Object does not exists"})
#
#         return Response({"post": "delete post " + str(pk)})
#
