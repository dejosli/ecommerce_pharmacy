from django.urls import path
from blog.views import post_detail, PostList

# app_name

app_name = 'blog'

# Create your urls here.

urlpatterns = [
    path('', PostList.as_view(), name='allblogs'),
    #path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', post_detail, name='post_detail'),
]
