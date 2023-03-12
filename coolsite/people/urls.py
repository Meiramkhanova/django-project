from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('artists/', artists, name='artists'),
    path('audition/', audition, name='audition'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
]
