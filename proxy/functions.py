import json
import os
import xmlrpc.client
from constants import *

context = None

def get_context():
    global context
    if(not context):
        url_context=f"{CONTEXT_SCHEME}://{CONTEXT_HOST}:{CONTEXT_PORT}"
        context = xmlrpc.client.ServerProxy(url_context)
    return context

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
def init_variables(context,api_variables):
    for item in api_variables:
        value = os.getenv(item)
        if(isinstance(value,int)):
            value=int(value)
        else:
            value=str(value)
        context.set(item,value)


def choose_service(context,model,available_services): #------- TODO ----------------
    pass

