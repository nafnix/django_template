# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.11
FROM library/python:${PYTHON_VERSION}-bookworm AS builder

ARG PYPI_MIRROR=https://pypi.org/simple
WORKDIR /tmp
COPY ./pyproject.toml ./
RUN <<EOT
    pip install pdm --upgrade --no-cache-dir -i ${PYPI_MIRROR}
    pdm lock -v
    pdm export --without-hashes -o ./requirements.txt --prod -v
EOT


FROM library/python:${PYTHON_VERSION}-bookworm

ARG DEBIAN_FRONTEND=noninteractive

ARG SOURCES_MIRROR=deb.debian.org
ARG SECURITY_SOURCE_MIRROR=deb.debian.org
RUN <<EOT
    sed -i "s/deb.debian.org\/debian$/${SOURCES_MIRROR}\/debian/g" /etc/apt/sources.list.d/debian.sources
    sed -i "s/deb.debian.org\/debian-security$/${SECURITY_SOURCE_MIRROR}\/debian-security/g" /etc/apt/sources.list.d/debian.sources
    apt update
    apt install -y --no-install-recommends libpq-dev gcc
    apt clean all
    rm -rf /var/lib/apt/lists/*
EOT

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

ARG PYPI_MIRROR=https://pypi.org/simple
COPY --from=builder /tmp/requirements.txt /tmp/requirements.txt
RUN pip install --upgrade --no-cache-dir -i ${PYPI_MIRROR} gunicorn
RUN pip install --upgrade --no-cache-dir -i ${PYPI_MIRROR} -r /tmp/requirements.txt

ARG USER=django
ENV DJANGO_STATIC_ROOT=/var/www/static \
    DJANGO_BASE_DIR=/website

COPY . ${DJANGO_BASE_DIR}
RUN <<EOT
    useradd -m -d ${DJANGO_BASE_DIR} -s /bin/bash ${USER}
    mkdir -p ${DJANGO_STATIC_ROOT} ${DJANGO_BASE_DIR}
    chown -R ${USER}:${USER} ${DJANGO_BASE_DIR} ${DJANGO_STATIC_ROOT}
EOT


USER ${USER}
WORKDIR ${DJANGO_BASE_DIR}
RUN <<EOT
    chmod +x ${DJANGO_BASE_DIR}/scripts/*
EOT
