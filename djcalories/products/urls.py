from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductsHome.as_view(), name='index'),
    path('<int:id>/', views.category, name='category'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('profile-<int:pk>/', views.profile, name='profile'),
    path('adding-<int:pk>/', views.adding_product, name='adding_product'),
    path('calories-added-<int:pk>/', views.calories_added, name='calories_added'),
]
