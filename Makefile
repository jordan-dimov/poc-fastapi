.DEFAULT_GOAL := build

lint:
	black app/ tests/
	flake8 app/ tests/
	mypy --ignore-missing-imports app/

test:
	pytest -vv tests/

build: lint test
