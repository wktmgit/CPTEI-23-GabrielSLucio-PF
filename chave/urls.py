from django.urls import path
from .views import ChavesView, ChaveAddView, ChaveUpDateView, ChaveDeleteView

urlpatterns = [
    path('chave', ChavesView.as_view(), name='chaves'),
    path('chave/adicionar/', ChaveAddView.as_view(), name='chave_adicionar'),
    path('<int:pk>/chave/editar/', ChaveUpDateView.as_view(), name='chave_editar'),
    path('<int:pk>/chave/apagar/', ChaveDeleteView.as_view(), name='chave_apagar'),
]
