FROM python:3.11.3-slim-buster
RUN set -xe && apt-get -yqq update && apt-get -yqq install python3-pip && pip3 install --upgrade pip 
COPY ./requirements.txt /flask_app/requirements.txt
WORKDIR /app
COPY . /app
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["db.py"]