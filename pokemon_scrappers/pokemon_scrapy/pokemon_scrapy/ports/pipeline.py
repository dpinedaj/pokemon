from abc import ABC, abstractmethod

class Pipeline(ABC):
    
    @abstractmethod
    def process_item(self):
        pass