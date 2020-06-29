.DEFAULT_GOAL := help
.PHONY: help devserve

help: ## this help dialog
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

devserve: ## serve app using Django dev server
	poetry run python manage.py runserver

makemigrations: ## make new Django migrations
	poetry run python manage.py makemigrations

migrate: ## run all Django migrations
	poetry run python manage.py migrate

