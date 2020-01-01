FROM tensorflow/tensorflow:latest-py3

RUN apt-get update

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y python3-tk

ADD ./requirements.txt /app/requirements.txt
RUN python3 -m pip install -r /app/requirements.txt

WORKDIR /app
RUN ["bash"]
