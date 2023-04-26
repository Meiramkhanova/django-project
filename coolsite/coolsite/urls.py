"""coolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from people.views import *
from django.urls import path
from rest_framework import routers
from coolsite import settings
from people.views import *
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'people', PeopleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('people.urls')),
    path('captcha', include('captcha.urls')),
    path('api/v1/', include(router.urls)), #https://127.0.0.1:8000/api/v1/people/
    # path('api/v1/peoplelist/', PeopleViewSet.as_view({'get': 'list'})),
    # path('api/v1/peoplelist/<int:pk>/', PeopleViewSet.as_view({'put':'update'})),
    # path('api/v1/peoplelist/', PeopleAPIList.as_view()),
    # path('api/v1/peoplelist/<int:pk>/', PeopleAPIUpdate.as_view()),
    # path('api/v1/peopledetail/<int:pk>/', PeopleAPIDetailView.as_view()),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)


