import os

RMQ_USER = str(os.getenv("RABBIT_MQ_USER"))
RMQ_PASSWORD = str(os.getenv("RABBIT_MQ_PASSWORD"))
RMQ_EXCHANGE = str(os.getenv("RABBIT_MQ_EXCHANGE"))

SERVING_HOST = str(os.getenv("EXTRACTOR_WORKER_HOST"))
SERVING_PORT = int(os.getenv("EXTRACTOR_WORKER_PORT"))

PROXY_HOST = (os.getenv("PROXY_HOST"))
PROXY_PORT = (os.getenv("PROXY_PORT"))
PROXY_SCHEME = (os.getenv("PROXY_SCHEME"))

CONTEXT_HOST = os.getenv("CONTEXT_RPC_HOST")
CONTEXT_PORT = os.getenv("CONTEXT_RPC_PORT")
CONTEXT_SCHEME =  os.getenv("CONTEXT_RPC_SCHEME")

PUBLISH_ERROR = "Error while trying to publish data"

# AVOID MODIFYING HERE, GOTO env/varnames.env and do your business
TWITTER_TOKEN_IDENTIFIER = str(os.getenv("TWITTER_TOKEN_IDENTIFIER"))

NUM_PROCS=int(os.getenv("NUM_PROCS"))
IMAGES_DIR=(os.getenv("IMAGES_DIR"))

IMAGES_URLS=(os.getenv("IMAGES_URLS_VAR"))

YOUTUBE_VIDEO_URL=(os.getenv("YOUTUBE_VIDEO_URLS_VAR"))
VIDEO_FRAGMENT_SIZE=(os.getenv("VIDEO_FRAGMENT_SIZE"))