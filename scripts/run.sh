#!/bin/bash
[ -z "$SERVER_PORT" ] && export SERVER_PORT=9010
export PYTHONPATH="$(pwd)":$PYTHONPATH
#poetry run langchain serve --host=0.0.0.0 --port=9010
langchain serve --host=0.0.0.0 --port="${SERVER_PORT}"