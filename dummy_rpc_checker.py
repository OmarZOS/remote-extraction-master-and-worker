import os
import xmlrpc.client

SERVING_HOST = str(os.getenv("PROXY_HOST"))
SERVING_PORT = int(os.getenv("PROXY_PORT"))

url="http://{}:{}".format(SERVING_HOST,SERVING_PORT)

proxy = xmlrpc.client.ServerProxy(url)

print(proxy.list_workers())


