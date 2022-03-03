FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/

# FROM ubuntu:18.04

# RUN apt-get update

# RUN apt-get upgrade

# RUN apt-get --yes --force-yes install nginx

# RUN rm /etc/nginx/sites-enabled/default

# COPY nginx.conf /etc/nginx/sites-enabled/

# EXPOSE 80

# CMD service nginx start && tail -f /dev/null