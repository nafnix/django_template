#! /usr/bin/env bash

set -ex

if [ -f "./pyproject.toml" ]; then
    pdm install -dv
    pdm run pre-commit install --install-hooks
fi
