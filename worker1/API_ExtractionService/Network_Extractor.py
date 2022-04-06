

import json
from networkx.readwrite import json_graph
from networkx.classes.function import is_empty
from constants import PUBLISH_ERROR

class NetworkExtractor:
    
    def __init__(self,api,context,structure,publisher,roadmap=[]):
        
        self.api=api
        self.context=context
        self.fullStructure=structure
        self.publisher=publisher
        self.roadmap=roadmap
    
    def publish_data(self,payload):
        # delivering payload
        try:
            self.publisher.publish(self.api,json.dumps(payload))
        except Exception as e:
            print(f"{PUBLISH_ERROR}: {str(e)}")
        
    def data_publisher(self,func):
        def wrapper_function(*args, **kwargs):
            func(*args,  **kwargs)
            if(not is_empty(self.graph)):
                payload = json.loads(json_graph.dumps(self.graph))
                payload["road_map"] = []
                self.publish_data(payload)
            else:
                print("Nothing to publish..")
        return wrapper_function

    # @property.setter
    # def proxy(self, prox : API_ExtractionProxy):
    #     self.myProxy = prox
    
    @property
    def getProxy(self):
        return self.proxy  

    @property
    def apiName(self):
        return self._apiName
    @apiName.setter
    def apiName(self,app):
        # 'setting'
        self._apiName = app

    def getStructureFilePath(self): 
        pass
        