import os
from xml.etree import ElementTree

import requests

from currencies.models import Currency


def get_currencies_from_xml():
    r = requests.get(os.environ.get("IMPORT_URL"))
    root = ElementTree.fromstring(r.text)
    currencies = dict()
    for child in root:
        currencies[child.find("Name").text] = float(child.find("Value").text.replace(",", "."))

    return currencies


def import_currencies():
    currencies = get_currencies_from_xml()
    db_currencies = Currency.objects.all()

    for db_currency in db_currencies:
        if db_currency.name not in currencies:
            db_currency.delete()

    for name, rate in currencies.items():
        try:
            db_currency = Currency.objects.get(name=name)
            db_currency.name = name
            db_currency.rate = rate
        except Currency.DoesNotExist:
            db_currency = Currency(name=name, rate=rate)

        db_currency.save()
