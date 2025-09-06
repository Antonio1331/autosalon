from django.contrib import admin
from django.urls import path
from salon import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.brand_list, name='brand_list'),
    path('cars/', views.car_list, name='car_list'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('brand/<int:pk>/', views.brand_cars, name='brand_cars'),
    path("cars/add/", views.add_car, name="add_car"),
    path('car/<int:pk>/delete/', views.delete_car, name='delete_car'),

]
