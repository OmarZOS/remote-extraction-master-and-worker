import json
import os
import xmlrpc.client

SERVING_HOST = str(os.getenv("CONTEXT_RPC_HOST"))
SERVING_PORT = int(os.getenv("CONTEXT_RPC_PORT"))
url="http://{}:{}".format(SERVING_HOST,SERVING_PORT)
context = xmlrpc.client.ServerProxy(url)

# SERVING_HOST = str(os.getenv("EXTRACTOR_WORKER_HOST"))
# SERVING_PORT = int(os.getenv("EXTRACTOR_WORKER_PORT"))
# url="http://{}:{}".format(SERVING_HOST,SERVING_PORT)
# worker = xmlrpc.client.ServerProxy(url)

# # Print list of available methods
# print(context.system.listMethods())
creds_0 = {"TWEET_CONSUM":str(os.getenv("TWEET_CONSUM")),
            "TWEET_SECRET":str(os.getenv("TWEET_SECRET")),
            "TWEET_KEY":str(os.getenv("TWEET_KEY")),
            "TWEET_ACCESS_SECRET":str(os.getenv("TWEET_ACCESS_SECRET"))}

creds_1 = {"TWEET_CONSUM":str(os.getenv("TWEET_CONSUM1")),
            "TWEET_SECRET":str(os.getenv("TWEET_SECRET1")),
            "TWEET_KEY":str(os.getenv("TWEET_KEY1")),
            "TWEET_ACCESS_SECRET":str(os.getenv("TWEET_ACCESS_SECRET1"))
            }

creds_2 = {"TWEET_CONSUM":str(os.getenv("TWEET_CONSUM2")),
            "TWEET_SECRET":str(os.getenv("TWEET_SECRET2")),
            "TWEET_KEY":str(os.getenv("TWEET_KEY2")),
            "TWEET_ACCESS_SECRET":str(os.getenv("TWEET_ACCESS_SECRET2"))
            }

creds_3 = {"TWEET_CONSUM":str(os.getenv("TWEET_CONSUM3")),
            "TWEET_SECRET":str(os.getenv("TWEET_SECRET3")),
            "TWEET_KEY":str(os.getenv("TWEET_KEY3")),
            "TWEET_ACCESS_SECRET":str(os.getenv("TWEET_ACCESS_SECRET3"))
            }

creds_0 = json.dumps(creds_0)
creds_1 = json.dumps(creds_1)
creds_2 = json.dumps(creds_2)
creds_3 = json.dumps(creds_3)

context.set("TwitterCredentials",creds_0)
# # context.set("TwitterCredentials",creds_1)
# context.set("TwitterCredentials",creds_2)
# # context.set("TwitterCredentials",creds_3)

context.set("Twitter_User_ID","1192946702891790336") # Abd Elmadjid Tebboune
context.set("Follower_Count_Limit","200")
context.set("Friend_Count_Limit","200")

print(context.get("Twitter_User_ID"))

# worker.StartHarvestingData("Twitter-service1",{"user":["id"]})



