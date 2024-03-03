#!/bin/bash
poetry run python src/pda/config/exec_create_all.py
poetry run python src/pda/api/__init__.py
