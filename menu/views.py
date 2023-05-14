from pyexpat import model
from typing import Any
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Category
from django.views.generic import ListView, CreateView, TemplateView, DetailView
from .forms import Regisration_Form, Category_Form, Product_Form
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

# add 2 view functions to see products and add products


#crud 
# Create your views here.
# def menu(request):
    # test = Category(name = 'Electronics')
    # test.save()
    # test = Category(name = 'Clothes')
    # test.save()
    # test = Category(name = 'Toys')
    # test.save()
    # test = Category(name = 'Music')
    # test.save()
    # test = Category(name = 'Pharmacy')
    # test.save()
    # categories = Category.objects.all()
    # return render(request, 'menu/index.html', 
    #     {
    #         'categories':categories,
    #         'title' : "main"
    #     })

class MenuView(ListView):
    model = Category
    template_name = 'menu/index.html'
    context_object_name = 'categories'
    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'main'
        return context

class Registration(CreateView):
    form_class = Regisration_Form
    template_name = 'menu/registor.html'
    success_url = reverse_lazy('menu')
    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'registration'
        return context
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        return reverse_lazy('menu')
    

class Add_Category(CreateView):
    form_class = Category_Form
    template_name = 'menu/category.html'
    # success_url = reverse_lazy('category')
    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'category'
        return context
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()
        return super(Add_Category, self).form_valid(form)

def category_delete(request, pk):
    category = Category.objects.get(pk = pk)
    category.delete()
    return redirect('menu')

class CategoryView(DetailView):
    template_name = 'menu/category_detail.html'
    model = Category
    context_object_name = 'category'

    # def get_queryset(self):
    #     return Category.objects.get(pk=pk)

class Profile_View(TemplateView):
    model = User
    template_name = 'menu/profile.html'
    # def __init__(self, **kwargs: Any) -> None:
    #     super().__init__(**kwargs)
    #     print(request.user)
    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'profile'
        context['categories'] = Category.objects.all()
        return context

class Login_User_View(LoginView):
    template_name = 'menu/login.html'
    form_class = AuthenticationForm
    def get_success_url(self) -> str:
        return reverse_lazy('menu')
    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'login'
        return context

    

def basket(request):
    categories = Category.objects.all()
    return render(request, 'menu/basket.html', 
        {
            'categories':categories,
            'title' : "basket"
        })


def wish_list(request):
    categories = Category.objects.all()
    return render(request, 'menu/wish_list.html', 
        {
            'categories':categories,
            'title' : "wish_list"
        })

def orders(request):
    categories = Category.objects.all()
    return render(request, 'menu/orders.html', 
        {
            'categories':categories,
            'title' : "orders"
        })

def exit(request):
    logout(request)
    return redirect('menu')



def delivery(request):
    print(request)
    raise Http404('<h1>Hello World</h1>')

def storage(request):
    print(request)
    raise Http404('<h1>Hello World</h1>')