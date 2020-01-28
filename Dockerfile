FROM python:3.7-alpine

COPY requirements.txt /

RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
 && pip install cython \
 && apk del .build-deps

RUN apk add --no-cache libressl-dev musl-dev libffi-dev libpng-dev freetype-dev build-base python-dev py-pip jpeg-dev zlib-dev libxml2-dev
RUN apk add --update --no-cache g++ gcc libxslt-dev

RUN pip install -r /requirements.txt

ENV TZ="America/Chicago"

COPY . /app

WORKDIR /app

RUN export PYTHONPATH=/app:$PYTHONPATH
RUN python setup.py install



CMD [ "python", "/app/bin/test.py" ]