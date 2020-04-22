from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from currencies.models import Currency
from currencies.pagination import CustomPagination
from currencies.serializers import CurrencySerializer
from currencies.tasks import import_currencies_task


class CurrenciesListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = CustomPagination


class CurrenciesDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CurrenciesImportView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        import_currencies_task.delay()
        return Response(status=status.HTTP_204_NO_CONTENT)
