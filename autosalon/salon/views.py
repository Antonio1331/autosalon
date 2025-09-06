from django.shortcuts import render, get_object_or_404, redirect
from .models import Brand, Car, Comment
from .forms import CarForm, CommentForm


def brand_list(request):
    brands = Brand.objects.all()
    return render(request, "salon/brand_list.html", {"brands": brands})

def car_list(request):
    cars = Car.objects.all()
    return render(request, "salon/car_list.html", {"cars": cars})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    comments = car.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
            return redirect('car_detail', pk=car.pk)
    else:
        comment_form = CommentForm()

    return render(request, "salon/car_detail.html", {
        "car": car,
        "comments": comments,
        "comment_form": comment_form
    })

def brand_cars(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    cars = brand.cars.all()
    return render(request, "salon/brand_cars.html", {"brand": brand, "cars": cars})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, "salon/add_car.html", {"form": form})


def delete_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        car.delete()
        return redirect('car_list')
    return render(request, 'salon/delete_car.html', {'car': car})

def add_car(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("car_list")
    else:
        form = CarForm()
    return render(request, "salon/add_car.html", {"form": form})

