FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache git

WORKDIR /app
COPY . /app/
RUN pip install .

ENTRYPOINT ["python", "-m", "co2meter_exporter"]
EXPOSE 9817
