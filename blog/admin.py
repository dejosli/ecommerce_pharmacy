from django.contrib import admin
from blog.models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
from blog.forms import PostForm, CommentForm

# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    form = PostForm
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    form = CommentForm
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_display_links = ('post', )
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
