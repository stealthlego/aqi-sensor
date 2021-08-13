FROM python:3

ADD sensor.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "./sensor.py" ]