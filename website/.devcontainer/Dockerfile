# syntax=docker/dockerfile:1
FROM mcr.microsoft.com/devcontainers/python:3.11-bookworm

ARG DEBIAN_FRONTEND=noninteractive
ARG SOURCES_MIRROR=deb.debian.org
ARG SECURITY_SOURCE_MIRROR=deb.debian.org
RUN <<EOT
    sed -i "s/deb.debian.org\/debian$/${SOURCES_MIRROR}\/debian/g" /etc/apt/sources.list.d/debian.sources
    sed -i "s/deb.debian.org\/debian-security$/${SECURITY_SOURCE_MIRROR}\/debian-security/g" /etc/apt/sources.list.d/debian.sources
    apt update
    apt install -y --no-install-recommends sudo git libpq-dev gcc
    apt autoremove -y
    apt clean
    rm -rf /var/lib/apt/lists/*
EOT


ARG PYPI_MIRROR=https://pypi.org/simple
RUN <<EOT
    python -m pip install -i ${PYPI_MIRROR} --upgrade pip
    pip config set global.index-url ${PYPI_MIRROR}
    pip install pdm
EOT

ARG USER=vscode
RUN <<EOT
    useradd -m -s /usr/bin/bash ${USER}
    echo "${USER} ALL=(ALL) NOPASSWD: ALL" >/etc/sudoers.d/${USER}
    chmod 0440 /etc/sudoers.d/${USER}
EOT

USER ${USER}
WORKDIR /home/${USER}
ARG ZSH_CUSTOM=/home/${USER}/.oh-my-zsh/custom
RUN <<EOT
    mkdir -p ${ZSH_CUSTOM}/plugins/pdm
    pdm completion zsh > ${ZSH_CUSTOM}/plugins/pdm/_pdm
    sed -i "s|^plugins=(|&pdm |" .zshrc
EOT
