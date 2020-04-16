from django.urls import path

from currencies.views import CurrenciesListView, CurrenciesDetailView, CurrenciesImportView

urlpatterns = [
    path("currencies/", CurrenciesListView.as_view()),
    path("currencies/<int:pk>", CurrenciesDetailView.as_view()),
    path("currencies/import", CurrenciesImportView.as_view()),
]
