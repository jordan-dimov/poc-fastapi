.DEFAULT_GOAL := lint


lint:
	black app/
	flake8 app/
	mypy --ignore-missing-imports app/
