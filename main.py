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
	clientPizza = [] #Lista de las pizzas

	while exit == False:
		pizza = Pizza() #Objeto pizza
		director = Kitchen() #Objeto cocina
		builder = ParticularPizzaBuilder(pizza) #Constructor de la pizza 		director.builder = builder
		clientPizza.append(pizza)
		
		print("""
			Pizza número """+ str(len(clientPizza)))
		Menu.seleccionar_tamaño(builder)
		Menu.showIngredientsMenu()
		Menu.selectIngredients(builder)
		exit = Menu.selectAnotherPizza()
		Menu.showAllTargetPizzaData(builder)
		
	Menu.showReceipt(clientPizza)
	
	print("""El monto total a pagar seria """ + str(Menu.getTotalPizzasPrice(clientPizza)))
	print("""¡Gracias por su compra! Regrese pronto""")

