.DEFAULT: compose

APP = restapi

test:
	@flake8 . --exclude .venv
	@pytest -W ignore::DeprecationWarning -W ignore::UserWarning

compose:
	@docker compose build
	@docker compose up
