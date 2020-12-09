from django.contrib import admin

from .models import Post, Category, Coment



class PostAdmin(admin.ModelAdmin): 
    list_display = ['title' ,'author', 'category', 'created']
    search_fields = ['title', 'content' ]
    list_filter = ('category','tags')



admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Coment)


