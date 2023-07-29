from __future__ import absolute_import, unicode_literals

import os

from celery import Celery


# 为“celery”程序设置默认的 Django 设置模块。
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("website")

# 在这里使用字符串意味着 worker 不必序列化子进程的配置对象。
# namespace='CELERY' 意味着所有与 celery 有关的配置键都应该有一个以 CELERY_ 开头的前缀
app.config_from_object("django.conf:settings", namespace="CELERY")

# 从所有已经注册的 Django 应用加载 tasks.py 模块，
# 有了它，就不再需要手动添加各个模块到 CELERY_IMPORTS 中
app.autodiscover_tasks()
