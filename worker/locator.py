import os

from worker.publisherImplementation import publisherImplementation

RMQ_USER = str(os.getenv("RABBIT_MQ_USER"))
RMQ_PASSWORD = str(os.getenv("RABBIT_MQ_PASSWORD"))

publisher = publisherImplementation(user=RMQ_USER,password=RMQ_PASSWORD)

class locator(object):
    def getPublisher():
        return publisher
