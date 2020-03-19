ROM python:3.6.10-alpine3.10

WORKDIR /usr/src/app

COPY metrics.py .

RUN apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev linux-headers \
    && pip install --no-cache-dir psutil

ENTRYPOINT ["python","metrics.py"]
CMD ["mem","cpu"]
