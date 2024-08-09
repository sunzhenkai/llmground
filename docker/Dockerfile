FROM python:3.12-slim

RUN apt update && apt install git -y
RUN pip install langchain==0.2.12 \
  langchain-cli==0.0.28 \
  langchain-community==0.2.11 \
  langchain-core==0.2.29  \
  uvicorn==0.23.2 \
  pydantic==2.8.2 \
  langserve==0.2.2 \
  langchain-ollama==0.1.1
#RUN pip install poetry==1.8.3
#RUN poetry config virtualenvs.create false
WORKDIR /data/llmground
COPY ./ ./
COPY ./scripts/run.sh ./
#RUN poetry install  --no-interaction --no-ansi --no-root

ENV SERVER_PORT=9015
EXPOSE 9015
ENTRYPOINT [ "/usr/bin/bash", "run.sh" ]