.DEFAULT: compose

APP = restapi

test:
	@flake8 . --exclude .venv
	@pytest -v -W ignore::DeprecationWarning -W ignore::UserWarning

compose:
	@docker compose build
	@docker compose up

heroku:
	@heroku container:login
	@heroku container:push -a python-rest web
	@heroku container:release -a python-rest web

logs:
	@heroku logs --tail -a python-rest