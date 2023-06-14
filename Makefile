.PHONY: all
all:
	$(MAKE) build
	$(MAKE) docker

.PHONY: build
build:
	$(MAKE) clean
	$(MAKE) prepare-dir
	python3.11 scripts/main.py

.PHONY: test
test:
	python3.11 scripts/test.py

.PHONY: prepare-dir
prepare-dir:
	mkdir output output/assets output/changelogs output/specs
	cp assets/* output/assets
	cp specs/* output/specs
	cp -r vendor/swagger-ui output/swagger-ui

.PHONY: clean
clean:
	rm -rf output

.PHONY: docker
docker:
	docker build -t wizard-api-docs:local .
	docker run --rm --name "wizard-api-docs" -p 8888:8080 wizard-api-docs:local

.PHONY: download-latest-spec
download-latest-spec:
	curl -Lo specs/3.24.1.json https://api-app.ds-wizard.org/swagger.json
