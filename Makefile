start:
	bash scripts/run.sh

image:
	docker build . -f docker/Dockerfile -t llmground

docker-run:
	docker run -p 9010:9010 llmground