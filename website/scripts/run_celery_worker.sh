#!/bin/sh
set -ex

celery -A config.celery worker -l info
