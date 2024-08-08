start:
	bash scripts/run.sh

image:
	docker build . -f docker/Dockerfile -t llmground

docker-run:
	docker run --rm --net=host -p 9015:9015 llmground