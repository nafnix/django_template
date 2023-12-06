# syntax=docker/dockerfile:1
FROM mcr.microsoft.com/devcontainers/python:3.11-bookworm

ARG DEBIAN_FRONTEND=noninteractive
ARG SOURCES_MIRROR=deb.debian.org
ARG SECURITY_SOURCES_MIRROR=deb.debian.org
RUN <<EOT
    sed -i "s/deb.debian.org\/debian$/${SOURCES_MIRROR}\/debian/g" /etc/apt/sources.list.d/debian.sources
    sed -i "s/deb.debian.org\/debian-security$/${SECURITY_SOURCES_MIRROR}\/debian-security/g" /etc/apt/sources.list.d/debian.sources
    apt update
    apt install -y --no-install-recommends sudo git libpq-dev gcc
    apt autoremove -y
    apt clean
    rm -rf /var/lib/apt/lists/*
EOT


ARG PYPI_MIRROR=https://pypi.org/simple
RUN <<EOT
    pip config set global.index-url ${PYPI_MIRROR}
    pip install pdm
EOT


ARG USER=vscode
ARG DEFAULT_SHELL=/bin/zsh
RUN <<EOT
    usermod -s ${DEFAULT_SHELL} ${USER}
    echo "${USER} ALL=(ALL) NOPASSWD: ALL" >/etc/sudoers.d/${USER}
    chmod 0440 /etc/sudoers.d/${USER}
EOT


USER ${USER}
ARG HOME=/home/${USER}
ARG ZSH=${HOME}/.oh-my-zsh
ARG ZSH_CUSTOM=${ZSH}/custom
WORKDIR ${HOME}
RUN <<EOT
    mkdir -p ${ZSH_CUSTOM}/plugins/pdm
    pdm completion zsh > ${ZSH_CUSTOM}/plugins/pdm/_pdm
    sed -i "s|^plugins=(|&pdm |" .zshrc
EOT


ARG OHMYZSH_REMOTE=https://github.com/ohmyzsh/ohmyzsh.git
RUN <<EOT
    git -C ${ZSH} remote set-url origin ${OHMYZSH_REMOTE}
    git -C ${ZSH} pull
EOT


ARG P10K_REMOTE=https://github.com/romkatv/powerlevel10k.git
RUN <<EOT
    mkdir -p ${ZSH_CUSTOM}/themes/
    git clone --depth=1 ${P10K_REMOTE} ${ZSH_CUSTOM}/themes/powerlevel10k
    sed -i 's|ZSH_THEME="devcontainers"|ZSH_THEME="powerlevel10k/powerlevel10k"|g' .zshrc
    echo 'POWERLEVEL9K_DISABLE_CONFIGURATION_WIZARD=true' >> .zshrc
EOT

ENV DJANGO_SETTINGS_MODULE=config.settings DEBUG=True
