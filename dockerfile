FROM python:3.7.9-slim-buster

ADD sensor.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "./sensor.py" ]