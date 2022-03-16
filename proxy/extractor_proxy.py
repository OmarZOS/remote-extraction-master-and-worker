
from API_ExtractionService.Proxies.API_ExtractionProxy import API_ExtractionProxy
from worker.locator import locator
from worker.constants import *
from proxy.functions import *


class extractorProxy(API_ExtractionProxy):
    
    context = locator.getContext()
    
    def __init__(self,args):
        initialiseTwitterTokens(self.context,TWITTER_TOKEN_IDENTIFIER)

    def StartHarvestingData(self,model):
        pass
    
    def cancelHarvesting(id):
        pass

    def getStructureFile(self):
        pass
    
    def addAttribute(self,attribute):
        self.dynamicStructure.add(attribute)
    
    def removeAttribute(self,attribute):
        self.dynamicStructure.discard(attribute)
        
        


