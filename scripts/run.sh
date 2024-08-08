#!/bin/bash
export PYTHONPATH="$(pwd)":$PYTHONPATH
poetry run langchain serve --host=0.0.0.0 --port=9010