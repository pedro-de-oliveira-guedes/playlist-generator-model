run:
	docker build -t playlist-generator-model .
	docker run -d -p 8080:8080 --name playlist-generator-model playlist-generator-model

stop:
	docker stop $(shell docker ps -q --filter ancestor=playlist-generator-model)
