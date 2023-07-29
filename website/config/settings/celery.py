from ._base import django_settings


CELERY_BROKER_URL = django_settings.REDIS_URL

CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TIMEZONE = django_settings.TIME_ZONE
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#broker-connection-retry
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
