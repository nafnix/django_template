#!/bin/sh
set -ex

celery -A config.celery beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
