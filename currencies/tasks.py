from currencies.celery import celery_app
from currencies.import_service import import_currencies


@celery_app.task
def import_currencies_task(*args, **kwargs):
    import_currencies()
