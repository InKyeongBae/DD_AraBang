from django.contrib import admin
from .models import Post, School, Community


class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name']


class CommunityAdmin(admin.ModelAdmin):
    list_display = ['name']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(School, SchoolAdmin)
admin.site.register(Community, CommunityAdmin)
admin.site.register(Post, PostAdmin)

