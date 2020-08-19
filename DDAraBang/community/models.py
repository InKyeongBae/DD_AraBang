from django.db import models
from user.models import User
from django.contrib.auth import get_user_model

class School(models.Model):
    # pass

    name = models.CharField( max_length=30)
    email_list = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록 시간")

    def __str__(self):
        return self.name


class All_Community(models.Model):
    # pass
    name = models.CharField(max_length=64, verbose_name="제목", blank=True)
    description = models.CharField(max_length=200, null= True, blank=True)

    def __str__(self):
        return self.name


class Community(models.Model):
    # pass
    name = models.CharField(max_length=64, verbose_name="제목", blank=True)
    description = models.CharField(max_length=200, null= True, blank=True)

    def __str__(self):
        return self.name


class Post (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(blank=True, upload_to="post_photos")
    title = models.CharField(max_length=64, verbose_name="제목")
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    community = models.ForeignKey(
        Community, on_delete=models.CASCADE, null=True)
    contents = models.TextField(verbose_name="내용")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="수정 시간")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록 시간")
    like_users = models.ManyToManyField(User, related_name='like_posts', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class All_Post (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(blank=True, upload_to="all_post_photos")
    title = models.CharField(max_length=64, verbose_name="제목")
    School = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    all_community = models.ForeignKey(
        All_Community, on_delete=models.CASCADE, null=True)
    contents = models.TextField(verbose_name="내용")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="수정 시간")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록 시간")
    like_users = models.ManyToManyField(User, related_name='all_like_posts', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title



class Comment(models.Model):
    content = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    all_content = models.ForeignKey(All_Post, on_delete=models.CASCADE, null=True, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comment_like = models.IntegerField(default=0)

    def __str__(self):
        return (self.user.username if self.user else "무명")+ "의 댓글"
