from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VeiculoViewSet, FuncionarioViewSet, ViagemViewSet, ManutencaoViewSet

router = DefaultRouter()
router.register(r'veiculos', VeiculoViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'viagens', ViagemViewSet)
router.register(r'manutencao', ManutencaoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Define a URL base da API
]