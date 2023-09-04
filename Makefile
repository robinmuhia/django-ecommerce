.PHONY: runserver, deps, deps-prod, migrations, migrate

deps:
	poetry env use 3.11.1
	poetry install

deps-prod:
	poetry config virtualenvs.create false
	poetry install --no-dev

runserver:
	poetry run python manage.py runserver

migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

superuser:
	poetry run python manage.py createsuperuser


deploy:
	docker-compose build
	docker-compose up -d

down:
	docker-compose down
