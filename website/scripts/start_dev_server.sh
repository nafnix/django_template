#! /usr/bin/env bash
set -ex
if command -v docker; then
    docker compose up -d
    sleep 1
fi
pdm run python manage.py migrate
pdm run python manage.py runserver
