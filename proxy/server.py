import json
from random import random
import threading
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client

from locator import locator
from constants import *
from functions import get_context,choose_service, get_session, init_variables, initialise_credentials, renovate_schema_index

available_workers = []

schemas = {}

current_tasks = [{"id":1}]

timers = {}

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Twitter init
initialise_credentials(get_context()
    ,TWITTER_TOKEN_IDENTIFIER
    ,TWITTER_TOKEN_FIELDS)

init_variables(get_context(),TWITTER_GLOBAL_VARIABLES)

initialise_credentials(get_context()
    ,FACEBOOK_TOKENS_IDENTIFIER
    ,FACEBOOK_TOKEN_FIELDS)

init_variables(get_context(),FACEBOOK_GLOBAL_VARIABLES)

initialise_credentials(get_context()
    ,LINKEDIN_TOKENS_IDENTIFIER
    ,LINKEDIN_TOKEN_FIELDS)

init_variables(get_context(),LINKEDIN_GLOBAL_VARIABLES)

print("Serving at {}:{}".format(SERVING_HOST,SERVING_PORT))
# Create server
with SimpleXMLRPCServer((SERVING_HOST, int(SERVING_PORT)),
                        requestHandler=RequestHandler) as server:

    server.register_introspection_functions()

    # Setting a context variable
    def setVariable(varname,value):
        return get_context().set(str(varname),value)
    server.register_function(setVariable, 'set')
    
    # Registering a worker
    @server.register_function(name='register_worker')
    def register_worker(worker_host,worker_port,schema):
        url = f"http://{worker_host}:{worker_port}"    
        if(url not in [k["url"] for k in available_workers]):
            available_workers.append({
                    "url":url,
                    # "client":xmlrpc.client.ServerProxy(url)
                })
            global schemas
            schemas = renovate_schema_index(schemas,schema,url)
            return True;
        print ("The worker is already suscribed..")
        # print (schemas)
        return True;
    
    # Registering a worker
    @server.register_function(name='show_schemas')
    def show_schemes():
        # print (schemas)
        return str(schemas);
    
    # Updating a worker
    @server.register_function(name='update_worker')
    def update_worker(worker_host,worker_port,schema):
        url = "http://{}:{}".format(worker_host,worker_port)
        available_workers.append({
                "url":url
                # ,"client":xmlrpc.client.ServerProxy(url)
            })
        global schemas
        schemas = renovate_schema_index(schemas,schema,url)
        return True;
    
    @server.register_function(name='get')
    def getVariable(varname):
        return get_context().get(varname)

    @server.register_function(name='get_all_vars')
    def get_all_vars():
        return get_context().get_all_vals()
    
    @server.register_function(name='start_harvesting_data')
    def start_harvesting_data(api_name,model,starting_node=None):
        for (k,v) in starting_node.items():
            get_context().set(k,v)
        # - : make a choice of a specific service name depending on the input model
        #----------------------------------------------------------------
        chosen_service = choose_service(api_name,schemas,model).partition(",")
        if(not chosen_service):
            return "Couldn't find a compatible extraction service"
        service_name=chosen_service[0]
        url = chosen_service[2]
        try:
            get_session(url).start_harvesting_data(api_name,service_name,model)
        except BaseException as e:
            return f"Error while starting job, {url}: {e}"
        return "Job started successfully";
        #current_tasks is invloved
    
    @server.register_function(name='get_service')
    def get_service(api=None):
        # print(locator.availableServices)
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

    @server.register_function(name='start_downloading_images')
    def start_downloading_images():
        index = random.randrange(len(available_workers))
        if index not in timers:
            worker = available_workers[index]["client"]
            timer = threading.Timer(2.0, worker.start_downloading_images)
            timer.start()
            timers[str(index)] = timer
        else:
            timer.start()
        return True

    @server.register_function(name='stop_downloading_images')
    def stop_downloading_images():
        for k in timers.keys():
            timers[k].cancel()
            timers.pop(k)
        return True;

    # Run the server's main loop
    server.serve_forever()



