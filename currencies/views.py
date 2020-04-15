from rest_framework import generics

from currencies.models import Currency
from currencies.serializers import CurrencySerializer


class CurrenciesListView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CurrenciesDetailView(generics.RetrieveAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

