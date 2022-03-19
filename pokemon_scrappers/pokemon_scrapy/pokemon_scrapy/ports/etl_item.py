from abc import ABC, abstractmethod

class EtlItem(ABC):
    
    @abstractmethod
    def process(self):
        pass
    
    @abstractmethod
    def save(self, session):
        pass