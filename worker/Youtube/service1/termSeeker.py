


import json
import os
from queue import Queue
import time
import networkx
import random
from helper import openURL

from .legacy.search_keyword import searchVideo
from .config import MAXDEMANDS, REGIONCODE, YOUTUBE_SEARCH_URL, YOUTUBE_TOKEN   # to become a context.. #one_of_the_somedays..


class termSeeker:

    # set the waiting time
    
    fullStructure = None
   

    @staticmethod
    def searchTerm(graph,fullSchema,termQueue,videoQueue,channelQueue,playlistQueue):
        
        termSeeker.fullStructure = fullSchema

        freshTerm = termQueue.get()
        print(freshTerm)
        # termSeeker.insertUser(user=freshUser,graph=graph)

        while True:
            # print("Abagain")
            
            sv = searchVideo(freshTerm, MAXDEMANDS , REGIONCODE , YOUTUBE_TOKEN)
            
            try:
            
                url_response = json.loads(openURL(YOUTUBE_SEARCH_URL, sv.params))
                nextPageToken = url_response.get("nextPageToken")
                sv.load_search_res(url_response)

                while nextPageToken:
                    sv.params.update({"pageToken": nextPageToken})
                    url_response = json.loads(openURL(YOUTUBE_SEARCH_URL, sv.params))
                    nextPageToken = url_response.get("nextPageToken")
                    sv.load_search_res(url_response)
                
                print("locked and loaded")
                for video in sv.videos:
                    if video["videoId"] in graph: #just to put less noise in the queue
                        continue
                    videoQueue.add(video)
                    print(video)
                # termSeeker.scrapVideos(sv.videos,graph,videoQueue)
                print("gone with videos")
                # termSeeker.scrapChannels(sv.channels,graph,channelQueue)
                for channel in sv.channels:
                    if channel["channelId"] in graph: 
                        continue
                    channelQueue.add(channel)
                    print(channel)
                print("gone with channels")
                # termSeeker.scrapPlaylists(sv.playlists,graph,playlistQueue)
                for playlist in sv.playlists:
                    if playlist["playlistId"] in graph: 
                        continue
                    playlistQueue.add(playlist)
                    print(playlist)
                print("gone with playlists")
                
            except Exception as ex: 
                
                print("\033[93m An exception has occured \030[90m")
                print(ex.__cause__)

                #emptying the queue to terminate the thread..
                while not termQueue.empty():
                    termQueue.task_done()
                    termQueue.get()
                    
            termQueue.task_done()
            freshTerm = termQueue.get()

    @staticmethod
    def scrapChannels(channels,graph,channelQueue):
        for channel in channels:
            if channel["channelId"] in graph: 
                continue
            channelQueue.add(channel)
            print(channel)
            

    @staticmethod
    def scrapPlaylists(playlists,graph,playlistQueue):
        for playlist in playlists:
            if playlist["playlistId"] in graph: 
                continue
            playlistQueue.add(playlist)
            print(playlist)


    @staticmethod
    def scrapVideos(vids,graph,videoQueue:Queue):
        for video in vids:
            if video["videoId"] in graph: #just to put less noise in the queue
                continue
            videoQueue.add(video)
            print(video)
