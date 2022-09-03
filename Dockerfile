FROM nginx:latest
COPY ./nginx/nginx-app.conf /etc/nginx/sites-available/
COPY ./gunicorn/ /etc/systemd/system/
#COPY nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /etc/nginx/sites-enabled/\
    && ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/

FROM python:3.9

ENV PYTHONUNBUFFERED 1
RUN apt-get -y update && apt-get clean

RUN mkdir algo_visualization_backend


ADD . /algo_visualization_backend/


RUN pip install --upgrade pip
RUN pip install -r ./algo_visualization_backend/requirements.txt

EXPOSE 8000

WORKDIR /algo_visualization_backend