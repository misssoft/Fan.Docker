# TO buid: docker build -t nihao . --no-cache
# To run: docker run -p 5080:80 nihao:latest

FROM ubuntu:18.04

MAINTAINER oxfordfun "info@oxfordfun.com"

RUN apt-get update \
 && apt-get install -y python3-pip python3-dev \
 && cd /usr/local/bin \
 && ln -s /usr/bin/python3 python \
 && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV NAME World

CMD ["python3", "app.py"]


