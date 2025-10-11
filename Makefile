.DEFAULT: compose

APP = restapi

test:
	@flake8 . --exclude .venv

compose:
	@docker compose build
	@docker compose up
