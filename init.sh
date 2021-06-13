#!/bin/sh

sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

# sudo ln -sf /home/box/web/etc/gunicorn.conf.py   /etc/gunicorn.d/test.conf.py
sudo ln -sf /home/box/web/etc/gunicorn.django.conf.py   /etc/gunicorn.d/test.django.conf.py
sudo /etc/init.d/gunicorn stop
# gunicorn -c /etc/gunicorn.d/test.conf.py hello:app
gunicorn -c /etc/gunicorn.d/test.django.conf.py ask.wsgi:application

sudo /etc/init.d/mysql start
