import os


CONTEXT_HOST = (os.getenv("CONTEXT_RPC_HOST"))
CONTEXT_PORT = int(os.getenv("CONTEXT_RPC_PORT"))

SERVING_HOST = (os.getenv("PROXY_HOST"))
SERVING_PORT = int(os.getenv("PROXY_PORT"))

TWITTER_TOKEN_IDENTIFIER = "TwitterCredentials"


