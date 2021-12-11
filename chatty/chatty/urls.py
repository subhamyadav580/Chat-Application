from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    path('privatechat/', include('privatechat.urls')),
    path('auth/', include('account.urls')),
]
