from rest_framework.viewsets import ModelViewSet

from hex.models import People
from hex.serializers import PeopleSerializer

class PeopleViewSet(ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer