
from django.contrib import admin

from .models import Meal, Category


class MealAdmin(admin.ModelAdmin): 
    list_display = ['name' ,'category', 'preperation_time', 'price']
    search_fields = ['name', 'description' ]
    list_filter = ('category','name')



admin.site.register(Meal, MealAdmin)
admin.site.register(Category)
