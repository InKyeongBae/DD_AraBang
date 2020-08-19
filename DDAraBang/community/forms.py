from django import forms
from . import models

class PostForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = ['title', 'contents', 'photo']

    # title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "제목"}))
    # contents = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "단디 알아방 커뮤니티 글을 작성해 주세요:)"}))
    # photo = forms.ImageField()
    # def clean(self):
    #     email = self.cleaned_data.get("title")
    #     password = self.cleaned_data.get("contents")
    #     return self.cleaned_data

class CommentForm(forms.ModelForm):
    # text = forms.TextInput(label = '댓글')

    class Meta:
        model = models.Comment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = "댓글"