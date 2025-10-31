from rest_framework import serializers
from .models import Veiculo, Funcionario, Viagem, Manutencao

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

class ViagemSerializer(serializers.ModelSerializer):
    motorista = serializers.StringRelatedField()
    veiculo_placa = serializers.CharField(source='veiculo.placa', read_only=True)
    veiculo_modelo = serializers.CharField(source='veiculo.modelo', read_only=True)
    
    class Meta:
        model = Viagem
        fields = [
            'id', 'motorista', 'veiculo', 'veiculo_placa', 'veiculo_modelo',
            'codigo_id', 'data_inicio', 'hora_inicio', 'data_termino', 'hora_termino',
            'destino', 'km'
        ]

class ManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manutencao
        fields = '__all__'
