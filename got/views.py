from rest_framework import generics, filters
from got.models import Battles
from got.serializers import BattleSerializer


class BattleList(generics.ListCreateAPIView):
    queryset = Battles.objects.all()
    serializer_class = BattleSerializer


class BattleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Battles.objects.all()
    serializer_class = BattleSerializer


class BattleListByYear(generics.ListAPIView):
    serializer_class = BattleSerializer

    def get_queryset(self):
        queryset = Battles.objects.all()
        year = self.request.query_params.get('year',None)
        if year is not None:
            queryset = queryset.filter(year__exact=int(year))
            return queryset


class BattleListBy(generics.ListAPIView):
    queryset = Battles.objects.all()
    serializer_class = BattleSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name','year')
