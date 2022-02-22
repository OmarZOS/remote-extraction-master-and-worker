import queue,pika,os

from publishingService.publishingService import publishingService
from pika.exchange_type import ExchangeType

RMQ_HOST = str(os.getenv("RABBIT_MQ_HOST"))
RMQ_USER = str(os.getenv("RABBIT_MQ_USER"))
RMQ_PASSWORD = str(os.getenv("RABBIT_MQ_PASSWORD"))
RMQ_PORT = str(os.getenv("RABBIT_MQ_PORT"))

class publisherImplementation(publishingService):

    def __init__(self,user=RMQ_USER,password=RMQ_PASSWORD,*args):   
        
        self.credentials = pika.PlainCredentials(user,password)
        self.connection= pika.BlockingConnection(pika.ConnectionParameters(host=RMQ_HOST,port=RMQ_PORT))#, credentials= self.credentials
        self.channel= self.connection.channel()
        self.channel.exchange_declare(exchange='data', exchange_type=ExchangeType.direct)
        # self.addQueue("Context","token")
    
    def addQueue(self,routeName,queueName):
        self.channel.queue_declare(queue= queueName)
        self.channel.queue_bind(exchange="data", queue=queueName, routing_key=routeName)
    
    def updateVariable(self):
        pass
    
    
    def publish(self,routeName,data):
        # print("publishing")
        self.channel.basic_publish(exchange="data",routing_key = routeName ,body = data)