from PizzaBuilder import PizzaBuilder
from Pizza import Pizza

class ParticularPizzaBuilder(PizzaBuilder):	
	pizza: Pizza

	def __init__(self,pizza):
		self.Pizza=pizza

	def getPizza(self):
		self.Pizza.list_parts()

	def setPizza(self,ingridient):
		self.Pizza.addIngridient('pimientos')
		

	def agregarJamon(self) -> None:
		pass

	def agregarChampiñones(self):
		print("hola soy un champiñon")

	def agregarPimientos(self):
		self.Pizza.addIngridient('pimientos')

	def agregarDobleQueso(self) -> None:
		pass

	def agregarAceitunas(self) -> None:
		pass

	def agregarPepperoni(self) -> None:
		pass

	def agregarSalchichon(self) -> None:
		pass
		