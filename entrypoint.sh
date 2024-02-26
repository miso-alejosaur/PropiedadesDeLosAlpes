#!/bin/bash
if $CELERY; then
    poetry run celery -A src.tasks worker -l INFO
else
    poetry run python src/pda/config/exec_create_all.py
    poetry run python src/pda/api/__init__.py
fi