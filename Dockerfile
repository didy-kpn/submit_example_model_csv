FROM python:latest
MAINTAINER Didy KUPANHY <d.kupanhy@gmail.com>

ADD config.yml .
ADD example_predictions.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD python predict.py
