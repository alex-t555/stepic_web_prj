#!/bin/sh

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

# sudo ln -sf /home/box/web/etc/gunicorn.conf.py   /etc/gunicorn.d/test.conf.py
sudo /etc/init.d/gunicorn stop
gunicorn -c etc/guniconr.conf.py hello:app

# sudo /etc/init.d/mysql start
