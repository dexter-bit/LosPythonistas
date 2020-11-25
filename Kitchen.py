from Builders.PizzaBuilder import PizzaBuilder
from abc import ABC, abstractmethod, abstractproperty

class Kitchen():
	def __init__(self) -> None:
		self._PizzaBuilder = None

	@property
	def builder(self) -> PizzaBuilder:
		return self._PizzaBuilder

	@builder.setter
	def builder(self, builder: PizzaBuilder) -> None:
		"""
		The Director works with any builder instance that the client code passes
		to it. This way, the client code may alter the final type of the newly
		assembled product.
		"""
		self._PizzaBuilder = PizzaBuilder

		