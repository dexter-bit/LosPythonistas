from Pizza import Pizza
from abc import ABC, abstractmethod, abstractproperty

class PizzaBuilder(object):
    @abstractmethod
    def getPizza(self) -> None:
        pass

    @abstractmethod
    def setPizza(self) -> None:
        pass

    @abstractmethod
    def addHam(self) -> None:
        pass

    @abstractmethod
    def addMushrooms(self) -> None:
        pass

    @abstractmethod
    def addPeppers(self) -> None:
        pass

    @abstractmethod
    def addDoubleCheese(self) -> None:
        pass

    @abstractmethod
    def addOlive(self) -> None:
        pass

    @abstractmethod
    def addPepperoni(self) -> None:
        pass

    @abstractmethod
    def addSalami(self) -> None:
        pass