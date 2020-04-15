from django.http import JsonResponse

from currencies.models import Currency


def currencies_list(request):
    currencies = Currency.objects.all()
    return JsonResponse({"result": list(currencies.values())})


def currencies_detail(request, pk):
    currency = Currency.objects.get(id=pk)
    return JsonResponse({"result": {
        "id": currency.id,
        "name": currency.name,
        "rate": currency.rate,
    }})
