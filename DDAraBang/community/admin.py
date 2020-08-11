from django.contrib import admin
from .models import Post, School, Community, All_Community, All_Post


class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name']


class CommunityAdmin(admin.ModelAdmin):
    list_display = ['name']


class All_CommunityAdmin(admin.ModelAdmin):
    list_display = ['name']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title']

class All_PostAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(School, SchoolAdmin)
admin.site.register(Community, CommunityAdmin)
admin.site.register(All_Community, All_CommunityAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(All_Post, All_PostAdmin)