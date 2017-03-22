PYTHON ?= $(shell which python3)
BUILD_DIR = sample
RESUME = resumes/kevin.yaml
ENV = dev

.PHONY: help

help:
	@echo "----------------------------------------------------------"
	@echo "make html: 	Makes the HTML file"
	@echo "make pdf: 	Makes the PDF file"
	@echo "make clean:	Cleans the directory"
	@echo "make setup: 	Sets up the environment"
	@echo "----------------------------------------------------------"

html:
	resume $(RESUME) --generate html -d $(BUILD_DIR)
	@echo "Done"

pdf:
	resume $(RESUME) --generate pdf -d $(BUILD_DIR)

clean:
	@rm -rf $(BUILD_DIR)
	@rm -rf dist
	@rm -rf .env

local:
	make clean
	virtualenv -p python3 $(ENV)
	. $(ENV)/bin/activate
	$(ENV)/bin/pip3 install -e .

setup:
	make homebrew
	brew install python3
	brew install Caskroom/cask/wkhtmltopdf
	make local

homebrew:
ifndef OUTPUT
	@echo "Installing homebrew..."
	/usr/bin/ruby -e "$$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
endif

