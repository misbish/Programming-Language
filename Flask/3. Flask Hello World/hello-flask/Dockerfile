FROM python:3.7-slim

WORKDIR /bishnu

COPY hello-flask.py.py /bishnu
COPY Dockerfile /bishnu
COPY requirements.txt /bishnu

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python","hello-flask.py"]