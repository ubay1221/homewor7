from django.shortcuts import render, redirect
from .models import Car


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def add_car(request):
    name = request.POST.get('name')
    model = request.POST.get('model')
    year = request.POST.get('year')

    if name is not None and model is not None and year is not None:
        Car.objects.create(
            name=name,
            model=model,
            year=year
        )
        return redirect('car_list')
    return render(request, 'cars/add_car.html')