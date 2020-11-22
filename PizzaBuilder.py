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
    def agregarJamon(self) -> None:
        pass

    @abstractmethod
    def agregarChampiñones(self) -> None:
        pass

    @abstractmethod
    def agregarPimientos(self) -> None:
        pass

    @abstractmethod
    def agregarDobleQueso(self) -> None:
        pass

    @abstractmethod
    def agregarAceitunas(self) -> None:
        pass

    @abstractmethod
    def agregarPepperoni(self) -> None:
        pass

    @abstractmethod
    def agregarSalchichon(self) -> None:
        pass