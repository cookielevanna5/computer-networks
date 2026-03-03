#!/usr/bin/env bash

pip install --no-index --find-links=/internal/wheels -r requirements-dev.txt
pre-commit install
