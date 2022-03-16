import os

RMQ_USER = str(os.getenv("RABBIT_MQ_USER"))
RMQ_PASSWORD = str(os.getenv("RABBIT_MQ_PASSWORD"))

SERVING_HOST = str(os.getenv("EXTRACTOR_WORKER_HOST"))
SERVING_PORT = int(os.getenv("EXTRACTOR_WORKER_PORT"))

PROXY_HOST = (os.getenv("PROXY_HOST"))

PROXY_PORT = (os.getenv("PROXY_PORT"))

TWITTER_TOKEN_IDENTIFIER = "TwitterCredentials"
RMQ_EXCHANGE = str(os.getenv("RABBIT_MQ_EXCHANGE"))