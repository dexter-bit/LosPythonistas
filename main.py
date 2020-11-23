from Kitchen import Kitchen
from Builders.ParticularPizzaBuilder import ParticularPizzaBuilder
from Pizza import Pizza
from Builders.PizzaBuilder import PizzaBuilder
import Menu

from abc import ABC, abstractmethod, abstractproperty
import colorama


class main():	
	exit = False
	Menu.print_header()
	clientPizza = []

	while exit == False:
		pizza = Pizza()
		director = Kitchen()
		builder = ParticularPizzaBuilder(pizza)
		director.builder = builder
		clientPizza.append(pizza)
		
		print("""
			Pizza número """+ str(len(clientPizza)))
		Menu.seleccionar_tamaño(builder)
		Menu.showIngredientsMenu()
		Menu.selectIngredients(builder)
		exit = Menu.selectAnotherPizza()
		Menu.showAllTargetPizzaData(builder)

	print("""
		El pedido tiene un total de """ + str(len(clientPizza)) + """ pizza(s) por un monto de """ + str(Menu.getTotalPizzasPrice(clientPizza)))
	print("""
		¡Gracias por su compra! Regrese pronto
		
		""")
