.DEFAULT_GOAL := help
.PHONY: help format lint doccheck typecheck test devserve

help: ## this help dialog
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

format: ## format with black
	poetry run black microblot/

lint: ## lint with flake8
	poetry run flake8 microblot/

doccheck: ## check code docs with pydocstyle
	poetry run pydocstyle microblot/

typecheck: ## check type hints with mypy
	poetry run mypy --strict microblot/**

test: ## run tests with pytest
	poetry run pytest --cov=microblot tests/

devserve: ## run dev server
	poetry run uvicorn microblot.main:app --reload
