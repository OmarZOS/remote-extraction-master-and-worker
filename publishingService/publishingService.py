

from abc import ABC, abstractmethod

class publishingService(ABC):
    def __init__(self, *args):
        super(publishingService, self).__init__(*args)
    @abstractmethod
    def updateVariable(self,**kwargs):
        pass
        

    








