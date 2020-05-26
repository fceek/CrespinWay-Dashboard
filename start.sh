#!/bin/bash
git fetch --all
git reset --hard origin/master
rm -f dashboard/settings.py
mv dashboard/settings.bak dashboard/settings.py
cp -f dashboard/settings.py dashboard/settings.bak
python3 manage.py migrate
python3 manage.py runserver 192.168.0.132:80 --insecure