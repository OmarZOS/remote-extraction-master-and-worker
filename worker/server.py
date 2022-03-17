import subprocess
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import json,os
from multiprocessing import  Process
import xmlrpc.client
from locator import locator
from constants import *

current_tasks = [{"id":1}]

urlProxy="http://{}:{}".format(PROXY_HOST,PROXY_PORT)
extraction_proxy = xmlrpc.client.ServerProxy(urlProxy)
print("Serving somewhere")

url_context="http://{}:{}".format(CONTEXT_HOST,CONTEXT_PORT)
context = xmlrpc.client.ServerProxy(url_context)


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
try:
    print("Serving at {}:{}".format(SERVING_HOST,SERVING_PORT))
    # Create server
    with SimpleXMLRPCServer((str(SERVING_HOST), int(SERVING_PORT)),
                            requestHandler=RequestHandler) as server:
        
        server.register_introspection_functions()
        
        @server.register_function(name='subscribe_in_proxy')
        def subscribe_in_proxy(self,model):#first things first
            extraction_proxy.register_worker(SERVING_HOST,SERVING_PORT,locator.availableServices)
            return True

        @server.register_function(name='change_proxy')
        def change_proxy(self,proxy_host,proxy_port):#first things first
            urlProxy="http://{}:{}".format(proxy_host,proxy_port)
            extraction_proxy = xmlrpc.client.ServerProxy(urlProxy)
            return True

        # Setting a context variable
        def setVariable(varname,value):
            pass
            # return context.set(varname,value)
        server.register_function(setVariable, 'set')
        
        def subscribe_service(api,service_name,instance,json_info):
            locator.availableServices[api][service_name]=json_info
            locator.setService("{}-{}".format(api,service_name),instance)
            return True;
        server.register_function(setVariable, 'subscribe_service')
                
        
        @server.register_function(name='StartHarvestingData')
        def StartHarvestingData(service,model):
            try:
                p = Process(target=locator.getService(service),
                            args=(context,model,locator.getPublisher(),))
                p.start()
                return p.pid
            
            except Exception :
                return False
            #current_tasks is invloved, don't forget to pass context object

        extraction_proxy.register_worker(SERVING_HOST,SERVING_PORT,locator.availableServices)

        # Run the server's main loop
        server.serve_forever()
except print(0):
    pass

