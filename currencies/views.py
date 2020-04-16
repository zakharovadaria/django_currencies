import requests
from xml.etree import ElementTree
from rest_framework import generics
from rest_framework.response import Response

from currencies.models import Currency
from currencies.pagination import CustomPagination
from currencies.serializers import CurrencySerializer


class CurrenciesListView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = CustomPagination


class CurrenciesDetailView(generics.RetrieveAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CurrenciesImportView(generics.GenericAPIView):
    def get(self, request):
        r = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
        root = ElementTree.fromstring(r.text)
        for child in root:
            name = None
            value = None

            for ch in child:
                if ch.tag.lower() == "name":
                    name = ch.text
                if ch.tag.lower() == "value":
                    value = ch.text.replace(",", ".")
                    value = float(value)

            if name and value:
                if not Currency.objects.filter(name=name):
                    currency = Currency(name=name, rate=value)
                    currency.save()

        return Response({"result": "true"})
