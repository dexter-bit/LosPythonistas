from Kitchen import Kitchen
from ParticularPizzaBuilder import ParticularPizzaBuilder
from Pizza import Pizza
from PizzaBuilder import PizzaBuilder

from abc import ABC, abstractmethod, abstractproperty
# import colorama

def print_header():
	print("""
		Universidad Católica Andrés Bello
		Ingeniería Informática
		Programación en Python - Proyecto #1

		Integrantes del equipo:
		Luis Pinto - CI: 25210435
		Dexter Ramos - CI: 24204991
		José Andrés Rodríguez Pérez - CI: 27.663.836
		Ángel Sucasas - CI: 28.027.948
		
		*****************************
		*       PIZZERIA UCAB       *
		*****************************
		""")

def seleccionar_tamaño():
	userResponse = ''

	print("""
		SELECCIONE EL TAMAÑO
		Opciones: Grande ( g ) Mediana ( m ) Personal ( p )""", end = ": ")
	userResponse = input()
	if userResponse == 'g' or userResponse == 'm' or userResponse == 'p':
		pass
	else:
		print(colorama.Fore.RED + """
			Debe seleccionar el tamaño correcto!!""")
		print(colorama.Style.RESET_ALL)
		seleccionar_tamaño()


def selectIngridients(pizza):
	userResponse = ''

	print("""
		SELECCIONE LOS INGREDIENTES
		Ingredientes:
		Jamón         (ja)
		Champiñones   (ch)
		Pimentón      (pi)
		Doble Queso   (dq)
		Aceitunas     (ac)
		Pepperoni     (pp)
		Salchichón    (sa)

		Indique el ingrediente (Pulse enter para terminar)""", end = ": ")
	userResponse = input()
	ingredientSelection(userResponse)
	
	"""if (userResponse == 'ja'): 

	elif (userResponse == 'ch'):

	elif userResponse == 'pi' or userResponse == 'dq' or userResponse == 'ac' or userResponse == 'pp' or userResponse == 'sa':
		seleccionar_ingredientes()
	else:
		print(colorama.Fore.RED + 
			Debe seleccionar un ingrediente correcto!!)
		print(colorama.Style.RESET_ALL)
		seleccionar_ingredientes()"""


class main():	
	"""builder.agregarPimientos()
	builder.getPizza()
	builder.setSize("grande")
	print("\n")
	builder.getSize()"""

	exit = False

	clientPizza = []
	while exit == False:
		pizza = Pizza()
		director = Kitchen()
		builder = ParticularPizzaBuilder(pizza)
		director.builder = builder
		

		print_header()
		seleccionar_tamaño()
		selecciectIngridients(pizza)
		