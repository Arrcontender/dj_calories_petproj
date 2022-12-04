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
    operations = Calculator.objects.all().filter(user_id=user.pk)
    context = {
        'user': user,
        'operations': operations,
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

# TODO got to fix this func
def calories_added(request, pk):
    weight = request.POST['weight']
    product_pk = pk
    current_user = request.user
    try:
        print('kek')
        # Calculator.objects.create(
        #     user_id=current_user.pk,
        #     product_id=product_pk,
        #     weight=weight,
        #     total_proteins=Products.objects.get(pk=product_pk).values('proteins') * weight,
        #     total_fats=Products.objects.get(pk=product_pk).values('fats') * weight,
        #     total_carbohydrates=Products.objects.get(pk=product_pk).values('carbohydrates') * weight,
        #     total_calories=Products.objects.get(pk=product_pk).values('calories') * weight
        #     ).save()
        new_rec = Calculator()
        new_rec.user_id = current_user.pk
        print(current_user.pk)
        new_rec.product_id = product_pk
        print(product_pk)
        new_rec.weight = weight
        print(weight)
        prod = Products.objects.get(pk=product_pk)
        print(prod)
        new_rec.total_proteins = F(prod.proteins) * weight
        print(F(prod.proteins) + weight)
        new_rec.total_fats = F(prod.fats) * weight
        print(6)
        new_rec.total_carbohydrates = F(prod.carbohydrates) * weight
        print(7)
        new_rec.total_calories = F(prod.calories) * weight
        print(F('prod.calories')*weight)
        new_rec.save()
        print('Done')
    except:
        pass
        # return HttpResponseNotFound('<h1>Ошибка при совершении операции, значение должно быть целочисленным</h1>')
    return redirect('index')









