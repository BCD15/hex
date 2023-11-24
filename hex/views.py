from rest_framework.viewsets import ModelViewSet

from hex.models import People, Avaliador,Equipe,Empresa
from hex.serializers import PeopleSerializer,AvaliadorSerializer, EquipeSerializer, EmpresaSerializer

class PeopleViewSet(ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    
class AvaliadorViewSet(ModelViewSet):
    queryset = Avaliador.objects.all()
    serializer_class = AvaliadorSerializer
    
class EquipeViewSet(ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer
    
class EmpresaViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer