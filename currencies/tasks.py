from celery import shared_task

from currencies.import_service import import_currencies


@shared_task
def import_currencies_task(*args, **kwargs):
    import_currencies()
