
from constants import *
import xmlrpc.client

context = None
proxy = None

def get_context():
    global context
    if(not context):
        url_context=f"{CONTEXT_SCHEME}://{CONTEXT_HOST}:{CONTEXT_PORT}"
        context = xmlrpc.client.ServerProxy(url_context)
    return context

def get_proxy():
    global proxy
    if(not proxy):
        url_proxy=f"{PROXY_SCHEME}://{PROXY_HOST}:{PROXY_PORT}"
        proxy = xmlrpc.client.ServerProxy(url_proxy)
    return proxy