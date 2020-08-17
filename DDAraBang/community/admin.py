from django.contrib import admin
from .models import Post, School, Community, All_Community, All_Post, Comment


class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name']

# class Email_BackAdmin(admin.ModelAdmin):
#     list_display = ['email_list']

class CommunityAdmin(admin.ModelAdmin):
    list_display = ['name']

class All_CommunityAdmin(admin.ModelAdmin):
    list_display = ['name']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title']

class All_PostAdmin(admin.ModelAdmin):
    list_display = ['title']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['text']


admin.site.register(School, SchoolAdmin)
# admin.site.register(Email_Back, Email_BackAdmin)
admin.site.register(Community, CommunityAdmin)
admin.site.register(All_Community, All_CommunityAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(All_Post, All_PostAdmin)
admin.site.register(Comment, CommentAdmin)