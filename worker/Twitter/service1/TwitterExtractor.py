from API_ExtractionService.Network_Extractor import NetworkExtractor

from networkx.classes import graph
from networkx.readwrite import json_graph
from Twitter.service1.UserExtractor import UserExtractor
# from coordinatesExtractor import CoordinateExtractor
# from worker.locator import locator
# from mediaExtractor import MediaExtractor
# from placeExtractor import PlaceExtractor
# from tweetExtractor import TweetExtractor
# from urlExtractor import URLExtractor

import json
import time
import tweepy
import os
import networkx as nx
from queue import Queue
from threading import Thread

from locator import locator

class TwitterExtractor(NetworkExtractor):
    
    consumer_key=[]
    consumer_secret=[]
    access_key=[]
    access_secret=[]
    
    auth = [0,]
    
    # 1192946702891790336 #Abd Elmadjid Tebboune
    # 1204126203654889472
    # 933256938
    # 367742122
    # 1259979718637621253
    # 259325103
    # 1253323792446701570
    # 2680659782
    # 366091257

    @NetworkExtractor.data_publisher
    def __init__(self,context,structure,publisher,roadmap):
        self.super().__init__("Twitter",context,structure,publisher,roadmap)
        
        self.graph = nx.DiGraph(self.createGraph())

        userAgent = Thread(target=UserExtractor.crawlUser, args=(self,context,self.graph,self.fullStructure,))
        userAgent.setDaemon(True)
        userAgent.start()
        userAgent.join()
        
        # tweetAgent = Thread(target=TweetExtractor.crawlTweet, args=(self.api,self.graph,self.fullStructure,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue))
        # tweetAgent.setDaemon(True)
        # tweetAgent.start()

        # coordinatesAgent = Thread(target=CoordinateExtractor.crawlCoordinates, args=(self.api,self.fullStructure,self.graph,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue))
        # coordinatesAgent.setDaemon(True)
        # coordinatesAgent.start()

        # placeAgent = Thread(target=PlaceExtractor.crawlPlace, args=(self.api,self.fullStructure,self.graph,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue))
        # placeAgent.setDaemon(True)
        # placeAgent.start()

        # urlAgent = Thread(target=URLExtractor.crawlURL, args=(self.api,self.fullStructure,self.graph,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue))
        # urlAgent.setDaemon(True)
        # urlAgent.start()

        # mediaAgent = Thread(target=MediaExtractor.crawlMedia, args=(self.api,self.fullStructure,self.graph,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue))
        # mediaAgent.setDaemon(True)
        # mediaAgent.start()

        # print("Extraction complete.")
        # self.save_json("Graph.json",self.graph)
        
        

    def getAuth(self):
        creds = json.loads(self.context.get("TwitterCredentials"))
        self.auth[0] = (tweepy.OAuthHandler(creds["TWEET_CONSUM"], creds["TWEET_SECRET"]))
        self.auth[0].set_access_token(creds["TWEET_KEY"], creds["TWEET_ACCESS_SECRET"])
        return self.auth[0]

    def createGraph(self):
        return nx.DiGraph()
        

    def connectAPI(key):
        pass

    def save_json(self,filename,graph):
        g = graph
        g_json = json_graph.node_link_data(g)
        json.dump(g_json,open(filename,'w'),indent=2)

        
# Function created to extract coordinates from tweet if it has coordinate info
# Tweets tend to have null so important to run check
# Make sure to run this cell as it is used in a lot of different functions below

    def extract_coordinates(row):
        if row['Tweet Coordinates']:
            return row['Tweet Coordinates']['coordinates']
        else:
            return None

# Function created to extract place such as city, state or country from tweet if it has place info
# Tweets tend to have null places so it is important to check
# Make sure to run this cell as it is used in a lot of different functions below

    def extract_place(row):
        if row['Place Info']:
            return row['Place Info'].full_name
        else:
            return None




if __name__=="__main__":
    import xmlrpc.client
    SERVING_HOST = str(os.getenv("CONTEXT_RPC_HOST"))
    SERVING_PORT = int(os.getenv("CONTEXT_RPC_PORT"))
    url="http://{}:{}".format(SERVING_HOST,SERVING_PORT)
    context = xmlrpc.client.ServerProxy(url)
    extractor = TwitterExtractor(context,{"user":["id",
                    ]})
    print("Auf wiedersehen..")
        
        

