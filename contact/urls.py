from django.urls import path
from contact.views import emailView, successView
# app_name
app_name = 'contact'

# Create your urls here.

urlpatterns = [
    path('email/', emailView, name='email'),
    path('success/', successView, name='success'),
]