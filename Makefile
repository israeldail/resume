PYTHON ?= $(shell which python3)
BUILD_DIR ?= sample
RESUME = resumes/kevin.yaml

.PHONY: clean html pdf

all: clean html pdf

html:
	resume $(RESUME) --generate html -d $(BUILD_DIR)
	@echo "Done"

pdf:
	resume $(RESUME) --generate pdf -d $(BUILD_DIR)

clean:
	@rm -rf ./build