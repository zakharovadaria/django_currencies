import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_currencies.settings")

celery_app = Celery(
    "currencies",
    broker=os.environ.get("CELERY_BROKER_URL"),
)

celery_app.conf.beat_schedule = {
    "import_currencies_task": {
        "task": "currencies.tasks.import_currencies_task",
        "schedule": crontab(hour=0, minute=0),
        "args": ()
    },
}

celery_app.autodiscover_tasks()
