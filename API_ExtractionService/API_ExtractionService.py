

from abc import ABC, abstractmethod

from API_Views.API_View import APi_View;

class API_ExtractionService(ABC):
    def __init__(self, apiName):
        self.apiName=apiName

    def serviceName(self):
        return self.apiName;

    def apiView(self):
        return self.apiView;
    
    def apiView(self, viewServ : APi_View ):
        self.apiView = viewServ
    
    
    def getStructureFilePath(self):
        return self.apiView.getStructureFile;




        
        
    

if __name__ == "__main__":    

    class azz(API_ExtractionService):
        pass    
    c = azz("tw")
    print(c.serviceName+"done")
