
from apps.user_app import urls
from django.contrib import admin
from django.urls import path, include
from apps.user_app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-app/', include(urls)),
    path('', include(urls))
]
