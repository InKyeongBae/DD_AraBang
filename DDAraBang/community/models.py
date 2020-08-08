from django.db import models

class School(models.Model):
    # pass
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록 시간")

    def __str__(self):
        return self.name


class Community(models.Model):
    # pass
    name = models.CharField(max_length=64, verbose_name="제목", blank=True)
    # School = models.ForeignKey(School, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Post (models.Model):
    # pass
    title = models.CharField(max_length=64, verbose_name="제목")
    School = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    community = models.ForeignKey(
        Community, on_delete=models.CASCADE, null=True)
    contents = models.TextField(verbose_name="내용")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="수정 시간")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록 시간")
    # writer = models.ForeignKey('', verbose_name="작성자", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
