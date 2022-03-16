from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import os
import xmlrpc.client

from locator import locator
from constants import *

available_workers = []

schemas = {}

current_tasks = [{"id":1}]

url="http://{}:{}".format(CONTEXT_HOST,CONTEXT_PORT)
context = xmlrpc.client.ServerProxy(url)

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)



try:
    print("Serving at {}:{}".format(SERVING_HOST,SERVING_PORT))
    # Create server
    with SimpleXMLRPCServer((str(SERVING_HOST), int(SERVING_PORT)),
                            requestHandler=RequestHandler) as server:

        server.register_introspection_functions()

        # Setting a context variable
        def setVariable(varname,value):
            return context.set(varname,value)
        server.register_function(setVariable, 'set')
        
        # Registering a worker
        @server.register_function(name='register_worker')
        def register_worker(worker_host,worker_port,schema):
            url = "http://{}:{}".format(worker_host,worker_port)
            try:
                if(url not in [k["url"] for k in available_workers]):
                    available_workers.append({
                            "url":url,
                            "client":xmlrpc.client.ServerProxy(url)
                        })
                    schemas[url] = schema
                    return True;
                print ("The worker is already suscribed..")
                # print (schemas)
                return True;
            except print(0):
                return False;
        
        # Updating a worker
        @server.register_function(name='update_worker')
        def update_worker(worker_host,worker_port,schema):
            url = "http://{}:{}".format(worker_host,worker_port)
            try:
                available_workers.append({
                        "url":url,
                        "client":xmlrpc.client.ServerProxy(url)
                    })
                schemas[url] = schema
                return True;
            except print(0):
                return False;
        
        @server.register_function(name='get')
        def getVariable(varname):
            return context.get(varname)
        
        @server.register_function(name='StartHarvestingData')
        def StartHarvestingData(self,model):
            available_workers[context.getStrategy("Scheduling").getFrom("Workers")].StartHarvestingData(model)
            #current_tasks is invloved
        
        @server.register_function(name='get_service')
        def get_service(api=None):
            print(locator.availableServices)
            try:
                if not api :
                    return locator.availableServices
                return locator.availableServices[api]
            except print(0):
                return False;
        
        @server.register_function(name='list_workers')
        def list_workers(api=None):
            print([k["url"] for k in available_workers])
            try:
                # if not api :
                return [k["url"] for k in available_workers]
                
                # return available_workers
            except print(0):
                return False;
        
        
        # Run the server's main loop
        server.serve_forever()
    

except print(0):
    print(0)
    pass

