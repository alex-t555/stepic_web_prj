#!/bin/sh

sudo /etc/init.d/mysql start

mysql -uroot -e "create database ask;"
mysql -uroot -e "grant all privileges on ask.* to 'box'@'localhost' with grant option;"

~/web/ask/manage.py makemigrations
~/web/ask/manage.py migrate
