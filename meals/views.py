from django.shortcuts import render
from .models import Meal, Category

def meal_list(request):
    meal_list = Meal.objects.all()
    categories = Category.objects.all()

    context = {
        'meal_list': meal_list, 
        'categories': categories,
    }

    return render(request, "meal/list.html", context)


def meal_detail(request, slug):
    meal_detail = Meal.objects.get(slug=slug)

    context = {
        'meal_detail': meal_detail
    }

    return render(request, "meal/detail.html", context)