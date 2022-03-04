#!/bin/bash
echo "ok"
service mariadb start
mysql -u root -ppass << EOFMYSQL
create database test;
EOFMYSQL
tail -f /dev/null