.DEFAULT: compose

APP = python-rest

test:
	@black .
	@flake8 . --exclude .venv
	@bandit -r . -x '/.venv/','/tests/'
	@pytest -v -W ignore::DeprecationWarning -W ignore::UserWarning

compose:
	@docker compose build
	@docker compose up

heroku:
	@heroku container:login
	@heroku container:push -a $(APP) web
	@heroku container:release -a $(APP) web

logs:
	@heroku logs --tail -a $(APP)
