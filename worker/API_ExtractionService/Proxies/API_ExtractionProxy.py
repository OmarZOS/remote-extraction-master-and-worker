from API_ExtractionService.API_ExtractionService import API_ExtractionService

class API_ExtractionProxy(API_ExtractionService):
    
    fullStructure = {}

    view = None
    apiName=""
    
    def StartHarvestingData(self,model):
        pass
    
    def cancelHarvesting(id):
        pass

    def getStructureFile(self):
        return self.view.viewstructureFilePath
    
    def addAttribute(self,attribute):
        self.dynamicStructure.add(attribute)
    
    def removeAttribute(self,attribute):
        self.dynamicStructure.discard(attribute)
        
        


