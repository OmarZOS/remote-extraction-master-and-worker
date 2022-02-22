import os
import xmlrpc.client

SERVING_HOST = str(os.getenv("CONTEXT_RPC_HOST"))
SERVING_PORT = int(os.getenv("CONTEXT_RPC_PORT"))
url="http://{}:{}".format(SERVING_HOST,SERVING_PORT)
context = xmlrpc.client.ServerProxy(url)
print(url)

# # Print list of available methods
# print(context.system.listMethods())

context.set("token",98)

print(context.get("token"))