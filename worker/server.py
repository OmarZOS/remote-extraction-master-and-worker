from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from multiprocessing import  Process
import xmlrpc.client
from locator import locator
from constants import *
from functions import *
import os
import constants

current_tasks = [{"id":1}]

print("Serving somewhere")

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
print(f"Serving at {SERVING_HOST}:{SERVING_PORT}")
print("binding to ")

# Create server
with SimpleXMLRPCServer((SERVING_HOST, int(SERVING_PORT)),
                        requestHandler=RequestHandler) as server:
    
    server.register_introspection_functions()
    
    @server.register_function(name='subscribe_in_proxy')
    def subscribe_in_proxy(): #first things first
        get_proxy().register_worker(SERVING_HOST,SERVING_PORT,locator.availableServices)
        return True

    @server.register_function(name='change_proxy')
    def change_proxy(proxy_scheme,proxy_host,proxy_port):#first things first
        os.environ["PROXY_SCHEME"] = str(proxy_scheme)
        constants.PROXY_SCHEME = proxy_scheme
        os.environ["PROXY_HOST"] = str(proxy_host)
        constants.PROXY_HOST = proxy_host
        os.environ["PROXY_PORT"] = str(proxy_port)
        constants.PROXY_PORT = proxy_port
        return True

    # Setting a get_context() variable
    def setVariable(varname,value):
        return get_context().set(varname,value)
    server.register_function(setVariable, 'set')
    
    def subscribe_service(api,service_name,instance,json_info):
        locator.availableServices[api][service_name]=json_info
        locator.setService(f"{api}",f"{service_name}",instance)
        return True;
    server.register_function(setVariable, 'subscribe_service')
    
    @server.register_function(name='start_harvesting_data')
    def start_harvesting_data(api_name,service_name,model):
        try:
            p = Process(target=locator.getService(api_name,service_name),
                        args=(get_context(),model,locator.getPublisher(),))
            p.start()
            return p.pid
        
        except Exception :
            return False
        #current_tasks is invloved, don't forget to pass get_context() object


    get_proxy().register_worker(SERVING_HOST,SERVING_PORT,locator.availableServices)

    # Run the server's main loop
    server.serve_forever()

