from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, User
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

from .models import Products, Category
from .forms import RegisterUserForm
# Create your views here.


class ProductsHome(ListView):
    model = Category
    template_name = 'products/index.html'
    context_object_name = 'categories'


def category(request, id):
    category_name = Category.objects.values_list('cat_name', flat=True).filter(pk=id)
    products_in_cat = Products.objects.all().filter(category=category_name[0]).order_by('name')
    paginator = Paginator(products_in_cat, 50)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products_in_cat': products_in_cat,
        'category_name': category_name[0],
        'page_obj': page_obj,
    }
    return render(request, 'products/category_id.html', context)


class ProfilePage(ListView):
    model = User
    template_name = 'products/profile.html'


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
