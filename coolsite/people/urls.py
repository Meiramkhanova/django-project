from django.urls import path

from .views import *

urlpatterns = [
    path('', PeopleHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('artists/', artists, name='artists'),
    path('addinfo/', AddInfo.as_view(), name='addinfo'),
    path('audition_people/', audition_people, name='audition_people'),
    path('accounts/login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', PeopleCategory.as_view(), name='category'),
    path('audition-all/',audition_all, name='audition-all'),
    ]
