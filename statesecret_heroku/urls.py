"""state_secret URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
   https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path  # For django versions from 2.0 and up
# ...
# подключаем тестовую вьюху (представление) в папке проекта
from statesecret_heroku.views import hello, main, map
from django.views import generic
# from django.contrib.flatpages import views


urlpatterns = [
    path('admin/', admin.site.urls),

    # тестовая вьюха (представление)
    path('', main),
    path('hello/', hello),
    path('map/', map),
    path('time/', generic.TemplateView.as_view(template_name="time.html")),

]

# urlpatterns += [
#     path('flat/', views.flatpage, {'url': '/flat/'}, name='flat'),
#     # path('license/', views.flatpage, {'url': '/license/'}, name='license'),
# ]

