from django import forms
from blog.models import Post, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'content', 'status')
        widgets = {
            'content': CKEditorUploadingWidget(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'body': CKEditorUploadingWidget(),
        }
