# 导入 Celery APP 以确保所有 @shared_task 装饰器会用到它
from .celery import app as celery_app


__all__ = ("celery_app",)
