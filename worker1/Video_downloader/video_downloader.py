
from copyreg import pickle
import json
from API_ExtractionService.Network_Extractor import NetworkExtractor
import networkx as nx
import cv2
import pafy
from constants import YOUTUBE_VIDEO_URL,VIDEO_FRAGMENT_SIZE
import cPickle

class Extractor(NetworkExtractor):
    
    def __init__(self,context,structure,publisher,roadmap):
        self.super().__init__("Youtube",context,structure,publisher,roadmap)
        self.graph = nx.DiGraph(self.createGraph())

    def stream_video(self,context,publisher):
        url = self.context.get(YOUTUBE_VIDEO_URL)
        vPafy = pafy.new(url)

        video_id = vPafy.videoid

        play = vPafy.getbest(preftype="webm")

        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # start the video
        cap = cv2.VideoCapture(play.url)

        start=0
        end = 0
        size = 0
        frames= []
        while (True):
            ret,frame = cap.read()
            size +=1
            end  +=1
            frames.append(frame)
            if size >= VIDEO_FRAGMENT_SIZE or size == frame_count:
                self.video_split(video_id,start,end,frames)
                # emptying the graph
                self.graph = nx.DiGraph(self.createGraph())
                frames=[]
                size = 0
                start = end

            # cv2.imshow('frame',frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    @NetworkExtractor.data_publisher
    def video_split(self,id,start,end,frames):
        chunk = pickle.dumps(frames)
        data = {
            "pickled_chunk":chunk
        }
        self.graph.add_nodes_from([f"{id}-{start}-{end}",data])
