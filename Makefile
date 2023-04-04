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
	mkdir output output/assets output/diffs output/specs
	cp assets/* output/assets
	cp specs/* output/specs

.PHONY: clean
clean:
	rm -rf output

.PHONY: docker
docker:
	docker build -t vknaisl/wizard-api-docs .
	docker run --rm --name "wizard-api-docs" -p 8888:80 vknaisl/wizard-api-docs