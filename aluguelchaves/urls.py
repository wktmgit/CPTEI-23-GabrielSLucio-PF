from django.contrib import admin
from django.urls import path, include

from home.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('funcionario.urls')),
    path('', include('chave.urls')),
    path('', include('cliente.urls')),
    path('', include('sala.urls')),
    path('', include('retirada.urls')),
]
