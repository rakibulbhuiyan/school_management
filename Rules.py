from abc import ABC,abstractclassmethod

class Rules(ABC):

    @abstractclassmethod
    def individualRules(self):
        pass