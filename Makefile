PYTHON ?= $(shell which python3)
BUILD_DIR ?= build
RESUME = resumes/kevin.yaml

.PHONY: clean html pdf

all: clean html pdf

html:
	resume $(RESUME) --generate html
	@echo "Done"

pdf:
	resume $(RESUME) --generate pdf

clean:
	@rm -rf ./build