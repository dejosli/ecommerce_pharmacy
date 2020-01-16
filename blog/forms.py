from django import forms
from blog.models import Post, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'slug', 'author', 'content', 'status')
        widgets = {
            'content': CKEditorUploadingWidget(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Enter your name'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control', 'placeholder':'Enter your email'}),
            'body': CKEditorUploadingWidget(),
        }
