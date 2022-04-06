FROM python:3.8-alpine

WORKDIR /code

COPY . /code

# RUN pip install --upgrade pip
RUN apk update && \
    apk add --virtual build-deps gcc musl-dev

RUN pip3 install -r requirements.txt


CMD ["python3", "/code/server.py"]
