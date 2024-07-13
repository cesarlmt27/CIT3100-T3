FROM python:3.12.3-slim-bullseye

WORKDIR /app

COPY ./entrypoint.sh /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/iot_platform

# ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT ["../entrypoint.sh"]