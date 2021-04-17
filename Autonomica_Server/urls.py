"""Autonomica_Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from autonomica import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),


    path('favicon.ico/', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    # Todos
    path('', views.home, name='home'),
    path('help/', views.help, name='help'),
    path('create/', views.createtodo, name='createtodo'),
    path('current/', views.currenttodos, name='currenttodos'),
    path('completed/', views.completedtodos, name='completedtodos'),
    path('autonomica/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('screen/<int:screen_pk>', views.viewscreen, name='viewscreen'),
    path('screen/fullscreen/<int:screen_pk>', views.fullscreen, name='fullscreen'),
    path('autonomica/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('autonomica/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
]
