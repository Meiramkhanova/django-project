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

from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

from people.views import *
from django.urls import path, re_path
from rest_framework import routers
from coolsite import settings
from people.views import *
from django.urls import path, include



# class MyCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(url=r'^{prefix}$',
#                       mapping={'get': 'list'},
#                       name='{basename}-list',
#                       detail=False,
#                       initkwargs={'suffix': 'List'}),
#         routers.Route(url=r'^{prefix}/{lookup}$',
#                       mapping={'get': 'retrieve'},
#                       name='{basename}-detail',
#                       detail=True,
#                       initkwargs={'suffix': 'Detail'})
#     ]
#
# router = routers.DefaultRouter()
# router.register(r'people', PeopleViewSet, basename='people')
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('people.urls')),
    path('captcha', include('captcha.urls')),
    # path('api/v1/', include(router.urls)), #https://127.0.0.1:8000/api/v1/people/
    # path('api/v1/peoplelist/', PeopleViewSet.as_view({'get': 'list'})),
    # path('api/v1/peoplelist/<int:pk>/', PeopleViewSet.as_view({'put':'update'})),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/people/', PeopleAPIList.as_view()),
    path('api/v1/people/<int:pk>/', PeopleAPIUpdate.as_view()),
    path('api/v1/peopledelete/<int:pk>/', PeopleAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path('r^auth', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('api/v1/token/verify', TokenVerifyView.as_view(), name = 'token_verify'),


]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)


