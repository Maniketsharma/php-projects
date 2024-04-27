from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class rectangle(shape):
    type = "rectangle"
    side = 13

    def __init__(self):
        self.length=19
        self.breadth=10

    def printarea(self):
        return self.length * self.breadth

rect1 = rectangle()
print(rect1.printarea())