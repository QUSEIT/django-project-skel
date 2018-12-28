.PHONY: default up build stop restart down migrate log enter_db

# Make sure the local file with docker-compose overrides exist.
#$(shell ! test -e \.\/.docker\/docker-compose\.override\.yml && cat \.\/.docker\/docker-compose\.override\.default\.yml > \.\/.docker\/docker-compose\.override\.yml)

# Create a .env file if not exists and include default env variables.
#$(shell ! test -e application\.env && cat application\.env.default > .docker\.env)

# Make all variables from the file available here.
include .env

# Defines colors for echo, eg: @echo "${GREEN}Hello World${COLOR_END}". More colors: https://stackoverflow.com/a/43670199/3090657
YELLOW=\033[0;33m
RED=\033[0;31m
GREEN=\033[0;32m
COLOR_END=\033[0;37m

default: up

up:
	@echo "${YELLOW}Build and run containers...${COLOR_END}"
	@echo "${YELLOW}${PROJECT_BASE_URL}${COLOR_END}"
	docker-compose up -d --remove-orphans

build:
	@echo "${YELLOW}Build containers...${COLOR_END}"
	docker-compose build

stop:
	@echo "${YELLOW}Stopping containers...${COLOR_END}"
	docker-compose stop

restart:
	@echo "${YELLOW}Restarting containers...${COLOR_END}"
	$(MAKE) -s down
	$(MAKE) -s up

down:
	@echo "${YELLOW}Removing network & containers...${COLOR_END}"
	docker-compose down -v --remove-orphans

migrate:
	@echo "${YELLOW}Making migrations...${COLOR_END}"
	docker-compose exec backend python manage.py makemigrations
	@echo "${YELLOW}Migrating...${COLOR_END}"
	docker-compose exec backend python manage.py migrate

log:
	@echo "${YELLOW}Printing logs...${COLOR_END}"
	docker-compose logs

enter_db:
	@echo "${YELLOW}Entering database...${COLOR_END}"
	docker-compose exec db psql ${DB_NAME} -U ${DB_USER} 
# https://stackoverflow.com/a/6273809/1826109
%:
	@:
