FROM python:3.5  AS build-env

ADD . /app
WORKDIR /app

RUN pip install -r ./requirements.txt

FROM gcr.io/distroless/python3
COPY --from=build-env /app /app
COPY --from=build-env /usr/local/lib/python3.5/site-packages /usr/local/lib/python3.5/site-packages

WORKDIR /app
ENV TZ="America/Chicago"
ENV PYTHONPATH=/app:/usr/local/lib/python3.5/site-packages

CMD ["/app/bin/test.py"] 
