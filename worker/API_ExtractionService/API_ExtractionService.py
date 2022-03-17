from abc import ABC, abstractmethod

from matplotlib.pyplot import get

class API_ExtractionService(ABC):
    def __init__(self,apiName ):
        self.apiName=apiName

    def serviceName(self):
        return self.apiName;

    def apiView(self):
        return self.apiView;
    
    def getStructureFilePath(self):
        return self.apiView.getStructureFile;

    

if __name__ == "__main__":    

    class azz(API_ExtractionService):
        pass    
    c = azz("tw")
    print(c.serviceName())
    print("done")
