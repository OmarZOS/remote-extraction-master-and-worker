
# This service is meant to publish extracted data to those who would listen..
# With RabbitMQ implementation, using a single queue means that data would be heard by one listener at a time..

import pika,os

from publishingService.publishingService import publishingService
from pika.exchange_type import ExchangeType
from constants import *


RMQ_HOST = str(os.getenv("RABBIT_MQ_HOST"))
RMQ_PORT = str(os.getenv("RABBIT_MQ_PORT"))
RMQ_USER = str(os.getenv("RABBIT_MQ_USER"))
RMQ_PASSWORD = str(os.getenv("RABBIT_MQ_PASSWORD"))
RMQ_EXCHANGE = str(os.getenv("RABBIT_MQ_EXCHANGE"))


class publisherImplementation(publishingService):
    
    def __init__(self,exchange=RMQ_EXCHANGE,user=RMQ_USER,password=RMQ_PASSWORD,*args):   
        
        self.credentials = pika.PlainCredentials(user,password)
        self.connection= pika.BlockingConnection(pika.ConnectionParameters(host=RMQ_HOST,credentials=self.credentials))#, credentials= self.credentials
        self.channel= self.connection.channel()
        self.channel.exchange_declare(exchange=exchange, exchange_type=ExchangeType.direct)
    
    def addQueue(self,routeName,queueName):
        self.channel.queue_declare(queue= queueName)
        self.channel.queue_bind(exchange=RMQ_EXCHANGE, queue=queueName, routing_key=routeName)
    
    def updateVariable(self):
        pass
    
    def publish(self,routeName,data):
        print("Eureka!!, es geht!")
        self.channel.basic_publish(exchange=RMQ_EXCHANGE,routing_key = routeName ,body = data)