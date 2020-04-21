import os
from xml.etree import ElementTree

import requests

from currencies.models import Currency


def import_currencies():
    r = requests.get(os.environ.get("IMPORT_URL"))
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
