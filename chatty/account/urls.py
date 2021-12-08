from django.urls import path

from account.views import register, login_view

urlpatterns = [
    path('register', register, name='register'),
    path('login', login_view, name='login')
]