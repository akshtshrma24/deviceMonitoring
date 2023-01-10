FROM python:3.8-slim-buster

WORKDIR /deviceMonitoring

EXPOSE 5002

COPY config.json . 

COPY /scraper/ .

RUN pip3 install --upgrade pip

RUN pip3 install prometheus-client

RUN apt-get update 

RUN apt-get install --assume-yes curl

CMD [ "python3", "scraper.py" ]