FROM python:latest

WORKDIR /home/kkk

COPY ./ ./

RUN apt-get update

RUN apt-get --yes --force-yes install vim

RUN pip install -r requirements.txt

EXPOSE 3000

ENTRYPOINT ["python","app.py"]