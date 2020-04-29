from currencies.celery import celery_app

if __name__ == "__main__":
    celery_app.send_task("currencies.tasks.import_currencies_task")
