FROM python:3.11-slim

RUN pip install poetry==1.8.3
RUN poetry config virtualenvs.create false
WORKDIR /data/llmground
COPY ./ ./
COPY ./scripts/run.sh ./
RUN poetry install  --no-interaction --no-ansi --no-root

EXPOSE 9010
ENTRYPOINT [ "/usr/bin/bash", "run.sh" ]