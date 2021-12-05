.DEFAULT_GOAL:=help
isort = isort dagserializer tests
black = black -S -l 80  dagserializer tests


.PHONY: install-dev
install-dev: ## Installs all dev requirements
	pip install -r requirementsdev.txt

.PHONY: format
format: ## Format with isort and black
	$(isort)
	$(black)

.PHONY: lint
lint: ## Lint with flake8, black, isort
	flake8 dagserializer/ tests/
	$(isort) --check-only --df
	$(black) --check --diff

.PHONY: mypy
mypy: ## Run mypy
	mypy dagserializer

.PHONY: test
test: ## Run all unittest
	python -m unittest discover tests


.PHONY: help
help: ## Show this help message.
	@echo
	@echo 'targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo