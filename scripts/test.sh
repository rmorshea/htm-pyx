#!/bin/bash
set -e

pytest \
    --cov=htm_pyx \
    --cov-config=.coveragerc
black \
    --verbose \
    --check \
    --exclude="(\.eggs|\.git|\.hg|\.mypy_cache|\.nox|\.tox|\.venv|_build|buck-out|build|dist|tests/.*html_coding\.py)" \
    .
flake8 src/py
mypy htm_pyx --config-file=mypy.ini
