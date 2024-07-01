from abc import ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def show(self):
        pass

class Child(Parent):
    def show(self):
        print("child class")

obj = Child()
obj.show()


