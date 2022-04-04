


import json
import os
from queue import Queue
import time
import networkx
import random
from helper import openURL

from .legacy.video_comments import VideoComment
from .config import MAXDEMANDS, REGIONCODE, YOUTUBE_COMMENT_URL, YOUTUBE_SEARCH_URL, YOUTUBE_TOKEN   # to become a context.. #one_of_the_somedays..


class VideoExtractor:

    # set the waiting time
    
    fullStructure = None
   

    @staticmethod
    def crawlVideo(graph,fullSchema,videoQueue):
        
        VideoExtractor.fullStructure = fullSchema

        freshVideo = videoQueue.get()

        while True:
            # print("Abagain")
            VideoExtractor.insertVideo(user=freshVideo,graph=graph)
            
            sv = VideoComment(freshVideo["videoId"], MAXDEMANDS , REGIONCODE , YOUTUBE_TOKEN)           
            
            try:
            
                url_response = json.loads(openURL(YOUTUBE_COMMENT_URL, sv.params))
                nextPageToken = url_response.get("nextPageToken")
                sv.load_comments(url_response)

                while nextPageToken:
                    sv.params.update({"pageToken": nextPageToken})
                    url_response = json.loads(openURL(YOUTUBE_COMMENT_URL, sv.params))
                    nextPageToken = url_response.get("nextPageToken")
                    sv.load_comments(url_response)

                
                # VideoExtractor.scrapComments(sv.comments,graph,videoQueue,freshVideo) #not today man..
                # VideoExtractor.scrapReplies(sv.replies,graph,videoQueue,freshVideo)
                
            except Exception as ex: 
                
                print("\033[93m An exception has occured \030[90m")
                print(ex.with_traceback)

                #emptying the queue to Videoinate the thread..
                while not videoQueue.empty():
                    videoQueue.task_done()
                    videoQueue.get()
                
            videoQueue.task_done()
            freshVideo = videoQueue.get()

    @staticmethod
    def insertVideo(graph,video):
        if video["videoId"] not in graph :
            graph.add_nodes_from(video["videoId"],[k for k in video.items()])

    @staticmethod
    def scrapVideos(vids,graph,videoQueue,freshVideo):
        for video in vids:
            if video["videoId"] not in graph: #just to put less noise in the queue
                videoQueue.add(video)
            
            graph.add_edge(video["videoId"],freshVideo["VideoId"],other= "includes")
            
            
            
            
