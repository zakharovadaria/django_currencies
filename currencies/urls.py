from django.urls import path

from currencies.views import currencies_list, currencies_detail

urlpatterns = [
    path("currencies/", currencies_list, name="currencies_list"),
    path("currencies/<int:pk>", currencies_detail, name="currencies_detail"),
]
