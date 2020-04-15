from django.urls import path

from currencies.views import CurrenciesListView, CurrenciesDetailView

urlpatterns = [
    path("currencies/", CurrenciesListView.as_view()),
    path("currencies/<int:pk>", CurrenciesDetailView.as_view()),
]
