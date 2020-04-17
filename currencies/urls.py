from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from currencies.views import CurrenciesListView, CurrenciesDetailView, CurrenciesImportView, Logout

urlpatterns = [
    path("currencies/", CurrenciesListView.as_view()),
    path("currencies/<int:pk>", CurrenciesDetailView.as_view()),
    path("currencies/import", CurrenciesImportView.as_view()),
    path("login", obtain_auth_token),
    path("logout", Logout.as_view()),
]
