FROM python:3.8-alpine

WORKDIR /code

# Install python/pip

RUN pip3 install redis
RUN pip3 install redis pika

COPY . /code

ENV CONTEXT_RPC_PORT="6060"
ENV CONTEXT_RPC_HOST="localhost"
ENV RABBIT_MQ_HOST="localhost"
ENV RABBIT_MQ_USER="omar"
ENV RABBIT_MQ_PASSWORD="omar"
ENV REDIS_HOST="localhost"
ENV REDIS_PORT="6379"
ENV ZOS_CONTEXT_ID="1"

ARG name=zos_context

ARG hostname=rabbitmq-broker

CMD ["python3", "/code/server.py"]