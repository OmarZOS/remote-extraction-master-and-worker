from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import json,os
import xmlrpc.client

from matplotlib.style import context


SERVING_PORT = int(os.getenv("EXTRACTOR_PROXY_PORT"))
SERVING_HOST = str(os.getenv("EXTRACTOR_PROXY_HOST"))

CONTEXT_HOST = str(os.getenv("CONTEXT_HOST"))
CONTEXT_PORT = int(os.getenv("CONTEXT_PORT"))

available_workers = []

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
    
    # Registering a worker
    @server.register_function(name='register_worker')
    def register_worker(worker_host,worker_port):
        url = "http://{}:{}".format(worker_host,worker_port)
        available_workers.append(xmlrpc.client.ServerProxy(url))
        return True;
    
    @server.register_function(name='getToken')
    def getVariable(varname):
        return context.get(varname)
    
    @server.register_function(name='StartHarvestingData')
    def StartHarvestingData(self,model):
        available_workers[context.getStrategy("Scheduling").getFrom("Workers")].StartHarvestingData(model)
        #current_tasks is invloved
        
        
    
    # server.register_function(getVariable, )
    


    # Run the server's main loop
    server.serve_forever()