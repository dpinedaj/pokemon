from abc import ABC, abstractmethod

class Entity(ABC):
    
    @abstractmethod
    def move(self):
        pass