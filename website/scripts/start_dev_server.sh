#! /usr/bin/env bash
set -ex

docker compose up -d
sleep 1
pdm run python manage.py migrate
pdm run python manage.py runserver
