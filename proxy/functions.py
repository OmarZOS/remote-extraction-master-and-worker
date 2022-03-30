import json
import os
from constants import *

# start with the identifier, then by fields
def initialise_credentials(context,*args):

    fields = {}
    
    for item in args[1]:
        fields[item] = str(os.getenv(TWEET_CONSUM_VARNAME)).split(",")

    creds_count = min(len(k) for k in fields.values() )  

    for i in range(creds_count): # for each column
        creds = {}
        for (k,v) in fields.items():
            creds[k]=v[i]
        creds_json = json.dumps(creds)
        context.set(args[0],creds_json)

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
    
