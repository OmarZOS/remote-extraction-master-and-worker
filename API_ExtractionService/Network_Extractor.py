

from abc import abstractmethod

from API_ExtractionService.Extractors.Transformers.API_Transformer import API_Transformer


class NetworkExtractor:


    @abstractmethod # it didn't work out this way..
    def __init__(self,apiNam,prox,structure):
        self.proxy = prox
        self._apiName=apiNam
        print("initialising transformer..")
        self.transformer = API_Transformer(self.initTransformer(structure))

    @abstractmethod
    def initTransformer(self,*args):
        pass

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
        self.getProxy.getStructureFilePath();
        
        