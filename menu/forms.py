from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Category, Products
from django import forms

class Regisration_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Category_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class Product_Form(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'characteristic', 'category_id']