from django.urls import path
from .views import SalasView, SalaAddView, SalaUpDateView, SalaDeleteView

urlpatterns = [
    path('sala', SalasView.as_view(), name='salas'),
    path('sala/adicionar', SalaAddView.as_view(), name='sala_adicionar'),
    path('<int:pk>/sala/editar/', SalaUpDateView.as_view(), name='sala_editar'),
    path('<int:pk>/sala/apagar/', SalaDeleteView.as_view(), name='sala_apagar'),

]
