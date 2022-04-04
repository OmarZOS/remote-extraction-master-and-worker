


import json
import os
from queue import Queue
import time
import networkx
import random
from helper import openURL

from .legacy.videos_channelid import channelVideo
from .config import MAXDEMANDS, REGIONCODE, YOUTUBE_SEARCH_URL, YOUTUBE_TOKEN   # to become a context.. #one_of_the_somedays..


class ChannelExtractor:

    # set the waiting time
    
    fullStructure = None
   

    @staticmethod
    def crawlChannel(graph,fullSchema,videoQueue,channelQueue):
        
        ChannelExtractor.fullStructure = fullSchema

        freshChannel = channelQueue.get()

        while True:
            # print("Abagain")
            
            ChannelExtractor.insertChannel(user=freshChannel,graph=graph)
            
            sv = channelVideo(freshchannel["channelId"], MAXDEMANDS , REGIONCODE , YOUTUBE_TOKEN)           
            
            try:
            
                url_response = json.loads(openURL(YOUTUBE_SEARCH_URL, sv.params))
                nextPageToken = url_response.get("nextPageToken")
                sv.load_channel_videos(url_response)

                while nextPageToken:
                    sv.params.update({"pageToken": nextPageToken})
                    url_response = json.loads(openURL(YOUTUBE_SEARCH_URL, sv.params))
                    nextPageToken = url_response.get("nextPageToken")
                    sv.load_channel_videos(url_response)

                
                ChannelExtractor.scrapVideos(sv.videos,graph,videoQueue,freshchannel)
                
            except Exception as ex: 
                
                print("\033[93m An exception has occured \030[90m")
                print(ex.with_traceback)

                #emptying the queue to channelinate the thread..
                while not channelQueue.empty():
                    
                    channelQueue.task_done()
                    
                    channelQueue.get()
                
            channelQueue.task_done()
            freshchannel = channelQueue.get()

    @staticmethod
    def insertChannel(freshChannel,graph):
        if freshChannel["channelId"] in graph :
            return
        graph.add_nodes_from(freshChannel["channelId"],[k for k in freshChannel.items()])

    @staticmethod
    def scrapVideos(vids,graph,videoQueue,freshchannel):
        for video in vids:
            if video["videoId"] not in graph: #just to put less noise in the queue
                videoQueue.add(video)
            
            graph.add_edge(video["videoId"],freshchannel["channelId"],other= "includes")
            
            
            
            
