start:
	bash scripts/run.sh

image:
	docker build . -f docker/Dockerfile -t sunzhenkai/llmground:$(tag)

docker-run:
	docker run --rm --net=host -p 9015:9015 sunzhenkai/llmground$(tag)

upload-image: image
	docker push sunzhenkai/llmground:$(tag)