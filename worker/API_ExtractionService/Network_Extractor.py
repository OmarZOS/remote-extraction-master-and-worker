

from abc import abstractmethod



class NetworkExtractor:

    @abstractmethod
    def connectAPI(key):
        pass

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
        'setting'
        self._apiName = app


    def getStructureFilePath(self): # just keeping the reference to respect Liskov principle
        pass
        