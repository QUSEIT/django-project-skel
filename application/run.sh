#!/usr/bin/bash

#export DB_NAME=<PLEASE REPLACE>
#export DB_HOST=<PLEASE REPLACE>
#export DB_PASSWORD=<PLEASE REPLACE>
#export DB_PORT=<PLEASE REPLACE,default postgresql:5432>
#export DB_USER=<PLEASE REPLACE>

export $(cat ../.env| xargs)
source ~/virtualenv/skel/django-project-skel/bin/activate
python manage.py runserver 0.0.0.0:$PORT
