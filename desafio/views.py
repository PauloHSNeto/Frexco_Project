from rest_framework import viewsets
from desafio.models import Region, Fruit
from desafio.serializer import RegionSerializer, FruitSerializer

class RegionsViewset(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class FruitsViewset(viewsets.ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
