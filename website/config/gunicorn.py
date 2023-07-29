import multiprocessing
from enum import StrEnum

from pydantic import BaseSettings, Field, IPvAnyAddress

from config.settings import DEBUG


class LogLevel(StrEnum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class GunicornSettings(BaseSettings):
    class Config:
        allow_mutation = False
        env_file_encoding = "utf-8"
        env_nested_delimiter = "_"
        case_sensitive = True
        env_prefix = "GUNICORN_"

    HOST: IPvAnyAddress = "0.0.0.0"
    PORT: int = Field(80, gt=0, le=65535)
    WORKERS_PER_CORE: int = 1
    WORKERS: int = max(multiprocessing.cpu_count(), 2)

    LOG_LEVEL: LogLevel = LogLevel.INFO

    ACCESS_LOG: str = "-"
    ERROR_LOG: str = "-"

    GRACEFUL_TIMEOUT: int = 120
    TIMEOUT: int = 120
    KEEP_ALIVE: int = 5


gunicorn_settings = GunicornSettings()

# Gunicorn config variables
reload = DEBUG
loglevel = gunicorn_settings.LOG_LEVEL
workers = gunicorn_settings.WORKERS
bind = f"{gunicorn_settings.HOST}:{gunicorn_settings.PORT}"
errorlog = gunicorn_settings.ERROR_LOG
worker_tmp_dir = "/dev/shm"
accesslog = gunicorn_settings.ACCESS_LOG
graceful_timeout = gunicorn_settings.GRACEFUL_TIMEOUT
timeout = gunicorn_settings.TIMEOUT
keepalive = gunicorn_settings.KEEP_ALIVE
