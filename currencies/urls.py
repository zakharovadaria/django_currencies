from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

from currencies.views import CurrenciesListView, CurrenciesDetailView, CurrenciesImportView

urlpatterns = [
    path("currencies/", CurrenciesListView.as_view()),
    path("currencies/<int:pk>", CurrenciesDetailView.as_view()),
    path("currencies/import", CurrenciesImportView.as_view()),
    path("login", token_obtain_pair),
    path("refresh", token_refresh),
]