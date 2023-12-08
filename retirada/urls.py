from django.urls import path
from .views import RetiradasView, RetiradaAddView, RetiradaUpDateView, RetiradaDeleteView, DevolucaoView

urlpatterns = [
    path('retirada', RetiradasView.as_view(), name='retiradas'),
    path('retirada/adicionar/', RetiradaAddView.as_view(), name='retirada_adicionar'),
    path('<int:pk>/retirada/editar/', RetiradaUpDateView.as_view(), name='retirada_editar'),
    path('<int:pk>/retirada/apagar/', RetiradaDeleteView.as_view(), name='retirada_apagar'),
    path('<int:pk>/retirada/devolucao/', DevolucaoView.as_view(), name='retirada_devolucao'),
]
