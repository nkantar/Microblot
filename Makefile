.DEFAULT_GOAL := help
.PHONY: help format lint 

help: ## this help dialog
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

format: ## format with black
	poetry run black microblot/

lint: ## lint with flake8
	poetry run flake8 microblot/
