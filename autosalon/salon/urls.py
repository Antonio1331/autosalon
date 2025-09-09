from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_list, name='car_list'),
    path('brands/', views.brand_list, name='brand_list'),
    path('brand/<int:pk>/', views.brand_cars, name='brand_cars'),
    path('create/', views.add_car, name='add_car'),
    path('update/<int:pk>/', views.update_car, name='update_car'),
    path('delete/<int:pk>/', views.delete_car, name='delete_car'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
]