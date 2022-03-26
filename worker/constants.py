import os

RMQ_USER = str(os.getenv("RABBIT_MQ_USER"))
RMQ_PASSWORD = str(os.getenv("RABBIT_MQ_PASSWORD"))
RMQ_EXCHANGE = str(os.getenv("RABBIT_MQ_EXCHANGE"))

SERVING_HOST = str(os.getenv("EXTRACTOR_WORKER_HOST"))
SERVING_PORT = int(os.getenv("EXTRACTOR_WORKER_PORT"))

PROXY_HOST = (os.getenv("PROXY_HOST"))

PROXY_PORT = (os.getenv("PROXY_PORT"))

TWITTER_TOKEN_IDENTIFIER = "TwitterCredentials"

CONTEXT_HOST = os.getenv("CONTEXT_RPC_HOST")
CONTEXT_PORT = os.getenv("CONTEXT_RPC_PORT")

PUBLISH_ERROR = "Error while trying to publish data"