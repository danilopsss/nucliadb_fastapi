app := main-app
test-app := test-app
dev-app := main-app-dev
docker-file-path := environment/
docker-from-file := docker-compose -f
run-dev-rm := run --rm --service-ports
docker-compose-file := docker-compose.yaml

@PHONY: clean-containers
clean-containers:
	echo "Cleaning containers...\n"
	@docker stop $$(docker ps -aq)
	@docker rm $$(docker container ls -aq)

@PHONY: run-dev
run-dev:
	$(docker-from-file) $(docker-file-path)$(docker-compose-file) $(run-dev-rm) $(dev-app)

@PHONY: run
run:
	$(docker-from-file) $(docker-file-path)$(docker-compose-file) up $(app) --build

@PHONY: run-test
run-test:
	$(docker-from-file) $(docker-file-path)$(docker-compose-file) up $(test-app) --build
	