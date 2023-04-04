from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .models import *
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin




class PeopleHome(DataMixin,ListView):
    model = People
    template_name = 'people/index.html'
    context_object_name = 'posts' #we can not write here menu, due to reason that it is dynamic

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main Page")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):  # to make a choice in panel admin to publish or not
        return People.objects.filter(is_published = True)

#def index(request):
 #   posts = People.objects.all()
  #  context = {
   #     'posts': posts,
    #    'menu': menu,
    #}
    #return render(request, 'people/index.html', context=context)

def audition_people(request):
    posts = Audition.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
    }
    return render(request, 'people/audition_people.html', context=context)

@login_required
def about(request):
    posts = People.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
    }
    return render(request, 'people/about.html', context=context)
def artists(request):
    return HttpResponse("The page about artists")


class AddInfo(LoginRequiredMixin ,DataMixin, CreateView):
    login_url = reverse_lazy('home')
    raise_exception = True
    form_class = AddPostForm
    template_name = 'people/addinfo.html'
    success_url = reverse_lazy('addinfo')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Add An Information'
        # context['menu'] = menu
        # return context
        c_def = self.get_user_context(title="Добавление статьи")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

#def audition(request):
    #if request.method == 'POST':
        #form = AddPostForm(request.POST,request.FILES)
       # if form.is_valid():
            #form.save()
            #return redirect('audition_people')
    #else:
        #form = AddPostForm()
    #return render(request, 'people/addinfo.html', {'menu': menu, 'title': 'Добавление статьи', 'form': form})
def login(request):
    return HttpResponse("Авторизация")


class ShowPost(DetailView):
    model = People
    template_name = 'people/post.html'
    slug_url_kwarg = 'post_slug'
    #pk_url_kwarg = 'post_pk'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


#def show_post(request, post_slug):
    #post = get_object_or_404(People, slug=post_slug)

    #context = {
        #'post': post,
        #'menu': menu,
       # 'title': post.title,
       #'cat_selected': post.cat_id,
   # }

    #return render(request, 'people/post.html', context=context)


class PeopleCategory(ListView):
    model = People
    template_name = 'people/index.html'
    context_object_name = 'posts'

    # def get_queryset(self):
    #     return People.objects.filter(cat_slug = self.kwargs['cat_slug'], is_published=True)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)

        return dict(list(context.items()) + list(c_def.items()))





#def show_category(request, cat_id):
    #posts = People.objects.filter(cat_id=cat_id)

    #if len(posts) == 0:
        #raise Http404()

    #context = {
        #'posts': posts,
        #'menu': menu,
        #'title': 'Отображение по рубрикам',
       # 'cat_selected': cat_id,
    #}

    #return render(request, 'people/index.html', context=context)

def audition_all(request):
    context = {
        'menu': menu,
    }
    return render(request, 'people/audition.html', context=context)