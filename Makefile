.DEFAULT_GOAL := help
.PHONY: help format lint doccheck typecheck test devserve worker build up upd logs queue down start stop sh djsh

help: ## this help dialog
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

format: ## [container] format with black
	poetry run black microblot/

lint: ## [container] lint with flake8
	poetry run flake8 microblot/

doccheck: ## [container] check code docs with pydocstyle
	poetry run pydocstyle microblot/

typecheck: ## [container] check type hints with mypy
	poetry run mypy --strict microblot/**

test: ## [container] run tests with pytest
	poetry run pytest --cov=microblot tests/

devserve: ## [container] run dev server
	poetry run python manage.py runserver 0.0.0.0:8000

worker: ## [container] run worker process
	poetry run python manage.py rqworker default --with-scheduler

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

djsh: ## docker-compose run --rm web poetry run python manage.py shell
	docker-compose run --rm web poetry run python manage.py shell
