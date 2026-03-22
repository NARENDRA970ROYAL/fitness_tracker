from django.shortcuts import render, redirect
from .models import FitnessTracker

def home(request):
    data = FitnessTracker.objects.all()
    return render(request, 'home.html', {'data': data})


def add_data(request):
    if request.method == "POST":
        exercise = request.POST.get('exercise')
        duration = request.POST.get('duration')
        calories = request.POST.get('calories')
        date = request.POST.get('date')

        FitnessTracker.objects.create(
            exercise=exercise,
            duration=duration,
            calories_burned=calories,
            date=date
        )
        return redirect('home')

    return render(request, 'add.html')