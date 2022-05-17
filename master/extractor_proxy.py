
from API_ExtractionService.Proxies.API_ExtractionProxy import API_ExtractionProxy
from proxy.locator import locator
from proxy.constants import *
from proxy.functions import *


class extractorProxy(API_ExtractionProxy):
    
    context = locator.getContext()
    
    def __init__(self,args):
        pass
    def start_harvesting_data(self,model):
        pass
    
    def cancelHarvesting(id):
        pass

    def getStructureFile(self):
        pass
    
    def addAttribute(self,attribute):
        self.dynamicStructure.add(attribute)
    
    def removeAttribute(self,attribute):
        self.dynamicStructure.discard(attribute)
        
        


