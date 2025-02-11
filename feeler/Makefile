# setup virtual environment for sentiment analysis application: 
# moodlens

VENV_NAME := .feelr_env
VENV_ACTIVATE := ../$(VENV_NAME)/Scripts/activate

.PHONY: setup activate install run all

setup:
	python -m virtualenv ../$(VENV_NAME)

activate:
	. $(VENV_ACTIVATE)

install:
	. $(VENV_ACTIVATE) && pip install -r requirements.txt

run:
	. $(VENV_ACTIVATE) && python manage.py runserver

migrate:
	python manage.py makemigrations && python manage.py migrate

all: setup install
	@echo "Run 'make activate' and 'source $(VENV_NAME)/bin/activate' to activate the virtual environment."
