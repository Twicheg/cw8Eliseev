FROM python:3.11

WORKDIR /cw8

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .


