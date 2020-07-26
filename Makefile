install:
	pip install -r requirements.txt

uninstall:
	pip freeze | xargs pip uninstall -y

run:
	python manage.py runserver

env:
	mkdir venv
	python -m venv ./venv

migrate:
	python manage.py migrate

user:
	python manage.py createsuperuser
