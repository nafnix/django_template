#!/bin/sh
set -ex

python manage.py collectstatic --noinput

sleep 1
python manage.py migrate

gunicorn -c config/gunicorn.py --print-config config.wsgi:application
gunicorn -c config/gunicorn.py config.wsgi:application
