# pull official base image
FROM python:3.8.3-alpine
LABEL maintainer=jfpinedap
 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && pip3 install --upgrade pip setuptools wheel \
    && pip3 install --no-cache-dir -r /requirements/local.txt

COPY ./compose/local/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint \
    && chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r//' /start \
    && chmod +x /start

ENTRYPOINT ["/entrypoint"]
