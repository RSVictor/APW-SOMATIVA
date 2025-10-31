from rest_framework import viewsets
from .models import Veiculo, Funcionario, Viagem, Manutencao
from .serializers import VeiculoSerializer, FuncionarioSerializer, ViagemSerializer, ManutencaoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ViagemFilter

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class ViagemViewSet(viewsets.ModelViewSet):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ViagemFilter

class ManutencaoViewSet(viewsets.ModelViewSet):
    queryset = Manutencao.objects.all()
    serializer_class = ManutencaoSerializer