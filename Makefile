install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=netwotk_vs_atoll --cov-report xml

lint:
	poetry run flake8 netwotk_vs_atoll

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

isort:
	poetry run isort netwotk_vs_atoll

.PHONY: install test lint selfcheck check build