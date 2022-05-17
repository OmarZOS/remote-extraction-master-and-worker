import json
import os
import xmlrpc.client
from constants import *

context = None

def get_context():
    global context
    url_context=f"{CONTEXT_SCHEME}://{CONTEXT_HOST}:{CONTEXT_PORT}"
    try:
        if(not context):
            context = connect_rpc(url_context)
    except BaseException as e:
        context = connect_rpc(url_context)
    return context

def get_session(url):
    session=None
    try:
        session = connect_rpc(url)
    except BaseException as e:
        session = connect_rpc(url)
        print (f"Something's wrong about the url {url},{str(e)}")
    return session
    
def renovate_schema_index(inverted_schema,schema,url):
    # print("I'll see u again meine liebste")
    for (api,services) in schema.items():
        for service in services:
            for (service_name,details) in service.items():
                # making sure we're talking about the schema
                if isinstance(details,dict): 
                    for (field,attributes) in details["schema"].items():
                        for attribute in attributes:
                                
                            if f"{api}-{field}-{attribute}" in inverted_schema:
                                inverted_schema[f"{api}-{field}-{attribute}"].add(f"{service_name},{url}")
                            else:
                                inverted_schema[f"{api}-{field}-{attribute}"]= set([f"{service_name},{url}"])
    return inverted_schema

def choose_service(api,inverted_schema,model): #------- Geschaft ---------
    schemes = []
    for (tag,fields) in model.items():
        for field in fields:
            print(f"{api}-{tag}-{field}")
            if f"{api}-{tag}-{field}" in inverted_schema:
                schemes.append(inverted_schema[f"{api}-{tag}-{field}"])
            # # danger!! to be removed, 
            # return schemes[f"{api}-{tag}-{field}"]
            # else:
            #     schemes.append(set([]))
    service_url = set.intersection(*schemes).pop()
    if(not service_url):
        return None
    return service_url

# start with the identifier, then by fields
def initialise_credentials(context,*args):
    
    fields = {}
    
    for item in args[1]:
        fields[item] = str(os.getenv(os.getenv(str(item)))).split(",")

    creds_count = min(len(k) for k in fields.values() )  

    for i in range(creds_count): # for each column
        creds = {}
        for (k,v) in fields.items():
            # k is the conventional varname, we have to get the real value 
            creds[str(os.getenv(k))]=v[i]
        creds_json = json.dumps(creds)
        context.set(str(args[0]),str(creds_json))

# api_variables_csv: a comma separated variable names
# for a specific API

def connect_rpc(url):
    return xmlrpc.client.ServerProxy(url)

def init_variables(context,api_variables):
    for item in api_variables:
        value = os.getenv(item)
        if(isinstance(value,int)):
            value=int(value)
        else:
            value=str(value)
        context.set(item,value)
