import decimal

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, User
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.db.models import *
from datetime import datetime


from .models import Products, Category, Calculator
from .forms import RegisterUserForm
# Create your views here.


class ProductsHome(ListView):
    model = Category
    template_name = 'products/index.html'
    context_object_name = 'categories'


def category(request, id):
    category_name = Category.objects.get(pk=id)
    products_in_cat = Products.objects.all().filter(category=category_name).order_by('name')
    paginator = Paginator(products_in_cat, 50)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products_in_cat': products_in_cat,
        'category_name': category_name,
        'page_obj': page_obj,
    }
    return render(request, 'products/category_id.html', context)


def profile(request, pk):
    user = User.objects.all().get(pk=pk)
    today_day = datetime.now().day
    operations = user.user_calculation.filter(date__day=today_day).order_by('date').reverse()
    print(operations)
    total_calories_by_day = sum([i.total_calories for i in operations])

    context = {
        'user': user,
        'operations': operations,
        'total_calories_by_day': total_calories_by_day
    }
    return render(request, 'products/profile.html', context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'products/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(LoginView):
    model = AuthenticationForm
    template_name = 'products/login.html'

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')


def adding_product(request, pk):
    if request.user.is_authenticated:
        product = Products.objects.get(pk=pk)

        context = {
            'product': product,
        }
        return render(request, 'products/adding_product.html', context)
    return redirect('category')


def calories_added(request, pk):
    weight = request.POST['weight']
    product_pk = pk
    current_user = request.user
    product = Products.objects.get(pk=product_pk)
    mass = int(weight) / 100
    mass = decimal.Decimal(mass)
    total_prots = product.proteins * mass
    total_f = product.fats * mass
    total_car = product.carbohydrates * mass
    total_cal = product.calories * mass
    x = Calculator.objects.create(
        weight=int(weight),
        total_proteins=total_prots,
        total_fats=total_f,
        total_carbohydrates=total_car,
        total_calories=total_cal
        )
    x.user.add(current_user.pk)
    x.product.add(product_pk)
    x.save()
    print('Well Done')
    return redirect('index')









