from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from currencies.authentication import BearerAuthentication
from currencies.models import Currency
from currencies.pagination import CustomPagination
from currencies.serializers import CurrencySerializer
from currencies.tasks import import_currencies_task


class CurrenciesListView(generics.ListAPIView):
    authentication_classes = (BearerAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = CustomPagination


class CurrenciesDetailView(generics.RetrieveAPIView):
    authentication_classes = (BearerAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CurrenciesImportView(generics.GenericAPIView):
    authentication_classes = (BearerAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        import_currencies_task.delay()
        return Response({"result": "true"})


class Logout(generics.GenericAPIView):
    authentication_classes = (BearerAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
