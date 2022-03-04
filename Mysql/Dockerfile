FROM debian

WORKDIR /home/

COPY ./ ./

RUN apt-get update

RUN apt-get --yes --force-yes install vim

RUN apt-get --yes --force-yes install mariadb-server

RUN apt-get --yes --force-yes install iputils-ping

RUN apt-get install -y dos2unix

RUN chmod +x /home/start.sh

RUN dos2unix /home/start.sh

CMD ["/home/start.sh"]