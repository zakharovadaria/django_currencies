from dotenv import load_dotenv

from currencies.celery import celery_app

load_dotenv()

if __name__ == "__main__":
    argv = ["currencies", "--beat", "--loglevel=info"]
    celery_app.worker_main(argv)
