from rest_framework.serializers import ModelSerializer

from hex.models import People, Avaliador,Equipe, Empresa

class PeopleSerializer(ModelSerializer):
    class Meta:
        model = People
        fields = "__all__"
        
class AvaliadorSerializer(ModelSerializer):
    class Meta:
        model = Avaliador
        fields = "__all__"

        
class EquipeSerializer(ModelSerializer):
    class Meta:
        model = Equipe
        fields = "__all__"
        
class EmpresaSerializer(ModelSerializer):
    class Meta:
        model = Empresa
        fields = "__all__"
