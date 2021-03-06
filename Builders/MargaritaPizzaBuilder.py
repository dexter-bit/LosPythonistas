from Pizza import Pizza
from Builders.PizzaBuilder import PizzaBuilder
from ingredients.Ham import Ham
from ingredients.Cheese import Cheese
from ingredients.Mushroom import Mushroom
from ingredients.Olive import Olive
from ingredients.Pepper import Pepper
from ingredients.Pepperoni import Pepperoni
from ingredients.Salami import Salami

class MargaritaPizzaBuilder(PizzaBuilder):	
	pizza: Pizza

	def __init__(self,pizza):
		self.Pizza= pizza
	
	def getPizza(self) -> None:
		return self.Pizza.getIngredients()

	def addHam(self) -> None:
		ham = Ham()
		self.Pizza.addIngredient(ham.name)
		self.Pizza.addPrice(ham.price)

	def addMushroom(self) -> None:
		mushroom = Mushroom()
		self.Pizza.addIngredient(mushroom.name)
		self.Pizza.addPrice(mushroom.price)

	def addPepper(self) -> None:
		pepper = Pepper()
		self.Pizza.addIngredient(pepper.name)
		self.Pizza.addPrice(pepper.price)

	def addDoubleCheese(self) -> None:
		doubleCheese = Cheese()
		self.Pizza.addIngredient(doubleCheese.name)
		self.Pizza.addPrice(doubleCheese.price)

	def addOlive(self) -> None:
		olive = Olive()
		self.Pizza.addIngredient(olive.name)
		self.Pizza.addPrice(olive.price)

	def addPepperoni(self) -> None:
		pepperoni = Pepperoni()
		self.Pizza.addIngredient(pepperoni.name)
		self.Pizza.addPrice(pepperoni.price)

	def addSalami(self) -> None:
		salami = Salami()
		self.Pizza.addIngredient(salami.name)
		self.Pizza.addPrice(salami.price)

	def setSize(self,size) -> None:
		self.Pizza.addSize(size)
	
	def setPrice(self,price) -> None:
		self.Pizza.addPrice(price)

	def getSize(self) -> None:
		return self.Pizza.getSize()

	def getPrice(self) -> None:
		return self.Pizza.getPrice()
	
	def getIngre(self) :
		self.Pizza.list_parts()
