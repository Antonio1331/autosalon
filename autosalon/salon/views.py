from django.shortcuts import render, get_object_or_404
from .models import Brand, Car

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, "salon/brand_list.html", {"brands": brands})

def car_list(request):
    cars = Car.objects.all()
    return render(request, "salon/car_list.html", {"cars": cars})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, "salon/car_detail.html", {"car": car})

def brand_cars(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    cars = brand.cars.all()
    return render(request, "salon/brand_cars.html", {"brand": brand, "cars": cars})
