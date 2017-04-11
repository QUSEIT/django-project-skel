#!/bin/sh
kill -9 `cat /data/pipaldata/appconfman_uwsgi.pid`
#killall uwsgi
uwsgi -i uwsgi.ini
