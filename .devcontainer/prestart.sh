#! /usr/bin/env bash

set -ex


if [ -f "./pyproject.toml" ]; then
    pdm install -dv
fi
