FROM nginx:latest
COPY ./nginx/nginx-app.conf /etc/nginx/sites-available/
#COPY nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /etc/nginx/sites-enabled/\
    && ln -s /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/

FROM python:3.9

ENV PYTHONUNBUFFERED 1
RUN apt-get -y update && apt-get clean

ADD . /algo_visualization_backend

WORKDIR /algo_visualization_backend

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000