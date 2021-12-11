from django.urls import path
from .views import privatechat

urlpatterns = [
    path('chat', privatechat, name='privatechat')
]