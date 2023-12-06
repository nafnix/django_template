from pathlib import Path

from pydantic import PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class DjangoSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix='DJANGO_',
        env_file=('.env', '.env.prod', '.env.dev'),
        env_file_encoding='utf-8',
        env_nested_delimiter='_',
        extra='ignore',
    )

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY: str

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG: bool = True
    ALLOWED_HOSTS: list[str] = []

    ROOT_URLCONF: str = 'config.urls'

    LANGUAGE_CODE: str = 'en-us'
    TIME_ZONE: str = 'UTC'
    USE_I18N: bool = True
    USE_TZ: bool = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.2/howto/static-files/
    STATIC_URL: str

    STATIC_ROOT: str | None = None

    DATABASE_URL: PostgresDsn
    REDIS_URL: RedisDsn


django_settings = DjangoSettings()  # type: ignore
