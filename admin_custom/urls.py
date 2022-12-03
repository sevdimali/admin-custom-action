from django.contrib import admin
from django.urls import path
from core.views import export

urlpatterns = [
    path('admin/', admin.site.urls),
    path('export/', export, name='export'),
]
