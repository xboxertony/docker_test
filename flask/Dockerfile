FROM python:latest

ENV PYTHONUNBUFFERED=1

WORKDIR /home/kkk

COPY ./ ./

RUN apt-get update

RUN apt-get --yes --force-yes install vim

RUN apt-get --yes --force-yes install iputils-ping

# RUN apt-get --yes --force-yes install mariadb-server

RUN pip install -r requirements.txt

CMD python -u app.py

# ENTRYPOINT ["python","app.py"]