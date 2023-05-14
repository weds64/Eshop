"""eshop URL Configuration

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
from django.urls import path
from menu.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MenuView.as_view(), name = 'menu'),
    path('basket/', basket, name = 'basket'),
    path('profile/', Profile_View.as_view(), name = 'profile'),
    path('wish_list/', wish_list, name = 'wish_list'),
    path('orders/', orders, name = 'orders'),
    path('delivery/', delivery, name = 'delivery'),
    path('storage/', storage, name = 'storage'),
    path('registore/', Registration.as_view(), name = 'registore'),
    path('logout/', exit, name = 'logout'),
    path('login/', Login_User_View.as_view(), name = 'login'),
    path('add_category/', Add_Category.as_view(), name = 'category'),
]
