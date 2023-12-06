import multiprocessing
from enum import StrEnum, auto

from pydantic import Field, IPvAnyAddress
from pydantic_settings import BaseSettings, SettingsConfigDict

from config.settings import DEBUG


class LogLevel(StrEnum):
    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    CRITICAL = auto()


class GunicornSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix='GUNICORN_',
        env_file=('.env', '.env.prod', '.env.dev'),
        env_file_encoding='utf-8',
        env_nested_delimiter='_',
        extra='ignore',
    )

    HOST: IPvAnyAddress = '0.0.0.0'  # type: ignore
    PORT: int = Field(80, gt=0, le=65535)
    WORKERS_PER_CORE: int = 1
    WORKERS: int = max(multiprocessing.cpu_count(), 2)

    LOG_LEVEL: LogLevel = LogLevel.INFO  # type: ignore

    ACCESS_LOG: str = '-'
    ERROR_LOG: str = '-'

    GRACEFUL_TIMEOUT: int = 120
    TIMEOUT: int = 120
    KEEP_ALIVE: int = 5


gunicorn_settings = GunicornSettings()  # type: ignore

# Gunicorn config variables
reload = DEBUG
loglevel = gunicorn_settings.LOG_LEVEL
workers = gunicorn_settings.WORKERS
bind = f'{gunicorn_settings.HOST}:{gunicorn_settings.PORT}'
errorlog = gunicorn_settings.ERROR_LOG
worker_tmp_dir = '/dev/shm'
accesslog = gunicorn_settings.ACCESS_LOG
graceful_timeout = gunicorn_settings.GRACEFUL_TIMEOUT
timeout = gunicorn_settings.TIMEOUT
keepalive = gunicorn_settings.KEEP_ALIVE
