import os

RMQ_USER = (os.getenv("RABBIT_MQ_USER"))
RMQ_PASSWORD = (os.getenv("RABBIT_MQ_PASSWORD"))

CONTEXT_HOST = (os.getenv("CONTEXT_RPC_HOST"))
CONTEXT_PORT = int(os.getenv("CONTEXT_RPC_PORT"))

SERVING_HOST = (os.getenv("PROXY_HOST"))
SERVING_PORT = int(os.getenv("PROXY_PORT"))

TWITTER_TOKEN_IDENTIFIER = "TwitterCredentials"


