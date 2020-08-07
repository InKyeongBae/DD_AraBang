from django.contrib import admin
from .models import *

@admin.register(Place)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']

@admin.register(School)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']

@admin.register(Test)
class PostAdmin(admin.ModelAdmin):
    list_display = ['school']
    list_display_links = ['school']

@admin.register(ReviewForm)
class ReviewFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'image','floor','advantage','disadvantage','water','light','noise','security','bug', 'money','recommend']