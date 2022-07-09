FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache git tini

WORKDIR /app
COPY . /app/
RUN pip install .

ENTRYPOINT ["tini", "python", "-m", "co2meter_exporter"]
EXPOSE 9817
