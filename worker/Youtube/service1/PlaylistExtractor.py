


import json
import os
from queue import Queue
from helper import openURL

class PlaylistExtractor:

    # set the waiting time
    
    fullStructure = None
   

    @staticmethod
    def crawlPlaylist(graph,fullSchema,playlistQueue):
        
        PlaylistExtractor.fullStructure = fullSchema

        freshPlaylist = playlistQueue.get()
        # PlaylistExtractor.insertUser(user=freshPlaylist,graph=graph)

        while True:
            # print("Abagain")
            
            # sv = PlaylistVideo(freshPlaylist, MAXDEMANDS , REGIONCODE , YOUTUBE_TOKEN)           
            
            try:
            
                freshPlaylist = playlistQueue.get()
                PlaylistExtractor.insertPlaylist(graph,freshPlaylist)
                
            except Exception as ex: 
                
                print("\033[93m An exception has occured \030[90m")
                print(ex.with_traceback)

                #emptying the queue to unPlaylistinate the thread..
                while not playlistQueue.empty():
                    
                    playlistQueue.task_done()
                    
                    playlistQueue.get()
                
            playlistQueue.task_done()
            freshPlaylist = playlistQueue.get()

    @staticmethod
    def insertPlaylist(graph,freshPlaylist):
        if freshPlaylist["playlistID"] not in graph:
            graph.add_nodes_from(freshPlaylist["playlistID"],[ k for k in freshPlaylist.items() ],other= "includes")
            
            
            
            
