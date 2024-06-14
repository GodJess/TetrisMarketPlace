from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('avtoriz/', views.avtoriz, name='avtoriz'),
    path('register/', views.register, name='register'),
    path('logout/', views.LogOut, name="logOut"),
    path('addprod/', views.AddProduct, name = "AddProduct"),
    path('loadPhoto/', views.LoadPhoto, name = 'loadPhoto'),
]
