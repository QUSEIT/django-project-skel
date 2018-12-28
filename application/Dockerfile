FROM python:3.6

RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
EXPOSE $PORT

RUN mkdir /quseit-server

COPY . /quseit-server
WORKDIR /quseit-server

RUN pip install -r ./requirements.txt

#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8001"]
#ENTRYPOINT gunicorn --reload apps.wsgi --timeout=30 --bind 0.0.0.0:$PORT --access-logfile -
