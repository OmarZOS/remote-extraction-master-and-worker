import json
import os
import xmlrpc.client 

from constants import *

url="http://{}:{}".format(CONTEXT_HOST,CONTEXT_PORT)
context = xmlrpc.client.ServerProxy(url)

class locator(object):
    
    # services = {}
    # services["Twitter-service1"] = TwitterExtractor

    with open("extractors.json") as f:
        availableServices = json.load(f)
    
    
    @staticmethod
    def getContext():
        return context
    
    @staticmethod
    def setService(self,service_name,instance):
        self.availableServices[service_name] = instance
    
    @staticmethod
    def getService(self,service_name):
        return self.availableServices[service_name]
