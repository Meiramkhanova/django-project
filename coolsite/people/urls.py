from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', PeopleHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('artists/', artists, name='artists'),
    path('addinfo/', AddInfo.as_view(), name='addinfo'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('audition_people/', audition_people, name='audition_people'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', PeopleCategory.as_view(), name='category'),
    path('audition-all/',audition_all, name='audition-all'),
    ]
