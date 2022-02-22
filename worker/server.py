from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import json,os
from multiprocessing import  Manager
import xmlrpc.client

SERVING_PORT = int(os.getenv("EXTRACTOR_WORKER_PORT"))
SERVING_HOST = str(os.getenv("EXTRACTOR_WORKER_HOST"))

CONTEXT_HOST = str(os.getenv("CONTEXT_HOST"))
CONTEXT_PORT = int(os.getenv("CONTEXT_PORT"))

current_tasks = [{"id":1}]

url="http://{}:{}".format(CONTEXT_HOST,CONTEXT_PORT)
context = xmlrpc.client.ServerProxy(url)

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer((SERVING_HOST, SERVING_PORT),
                        requestHandler=RequestHandler) as server:

    server.register_introspection_functions()

    # Setting a context variable
    def setVariable(varname,value):
        return context.set(varname,value)
    server.register_function(setVariable, 'set')
    
    @server.register_function(name='StartHarvestingData')
    def StartHarvestingData(model):
        #current_tasks is invloved, don't forget to pass context object
        pass

    # Run the server's main loop
    server.serve_forever()