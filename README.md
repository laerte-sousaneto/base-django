# Summary
This is a sample application setup with Django Framework and Postgres. The following are services used
for production: Heroku web service, and Heroku Postgres add-on.

# Development Setup

## Django Setup
1. Create a virtualenv: `make env`
1. Install packages: `make install`

## Database
1. Install Postgres and pgAdmin (optional) - [Download](https://www.postgresql.org/download/)
1. Update schemas: `make migrate`
1. Create super user: `make user`

## Web Server
To run web server: `make run`

# Initial release to heroku
1. Add environment variables:
```
ENVIRONMENT: PRODUCTION
SECRET_KEY: [Use secret generator tool]
```
[Secret Generator Tool](https://miniwebtool.com/django-secret-key-generator/)
1. Add Heroku Postgres add-on: https://elements.heroku.com/addons/heroku-postgresql
1. Deploy

# For Windows Environments (Optional)
1. Install Chocolatey - [Instructions](https://chocolatey.org/install)
1. Install make command: `choco install make`