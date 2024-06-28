import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'librishop.envs.development')
app = Celery('librishop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update(
    CELERY_BROKER_URL='amqp://guest:guest@rabbitmq:5672//',
    CELERY_RESULT_BACKEND='redis://redis:6379/0',
)
app.autodiscover_tasks()
