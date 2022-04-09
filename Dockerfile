FROM python:latest
LABEL maintainer="Didy"

ADD config.yml .
ADD example_predictions.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD python predict.py
