.DEFAULT_GOAL := help
.PHONY: help devserve worker makemigrations migrate flush super djsh format test lint build up upd logs queue down start stop sh

help: ## this help dialog
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

devserve: ## [container] serve app using Django dev server
	poetry run python manage.py runserver 0.0.0.0:8000

worker: ## [container] run worker process
	poetry run python manage.py rqworker default

makemigrations: ## [container] make new Django migrations
	poetry run python manage.py makemigrations

migrate: ## [container] run all Django migrations
	poetry run python manage.py migrate

flush: ## [container] flush DB
	poetry run python manage.py flush --noinput

super: ## [container] create superuser
	poetry run python manage.py createsuperuser

djsh: ## [container] open Django shell
	poetry run python manage.py shell

format: ## [container] run Black over everything
	poetry run black .

test: ## [container] poetry run python manage.py test
	PYTHONPATH="${PYTHONPATH}:/" poetry run pytest

lint: ## [container] poetry run flake8 .
	poetry run flake8 .

build: ## docker-compose build
	docker-compose build

up: ## docker-compose up
	docker-compose up

upd: ## docker-compose up --detach
	docker-compose up --detach

logs: ## docker-compose logs --follow
	docker-compose logs --follow

queue: ## docker-compose run --rm web poetry run python manage.py rqstats --interval=1
	docker-compose run --rm web poetry run python manage.py rqstats --interval=1

down: ## docker-compose down
	docker-compose down

start: ## docker-compose start
	docker-compose start

stop: ## docker-compose stop
	docker-compose stop

sh: ## docker-compose run --rm web /bin/sh
	docker-compose run --rm web /bin/sh
