#!/bin/bash
cd src/bff_investigacion
poetry run uvicorn main:app --host 0.0.0.0

