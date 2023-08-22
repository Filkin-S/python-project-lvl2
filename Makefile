install:
	poetry install

lint:
	poetry run flake8 gendiff

text:
	poetry run pytest

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build
