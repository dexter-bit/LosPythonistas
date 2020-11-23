from Kitchen import Kitchen
from ParticularPizzaBuilder import ParticularPizzaBuilder
from Pizza import Pizza
from PizzaBuilder import PizzaBuilder

from abc import ABC, abstractmethod, abstractproperty
# import colorama

def selectAnotherPizza():
	print("""
		¿Desea continuar?[s/n]: """)
	userResponse = input()
	if (userResponse == "s"):
		return False
	if (userResponse == "n"):
		return True 
	

def chooseIngredient(choosenIngredients,builder):
	if choosenIngredients == "ja":
		builder.addHam()		
	elif choosenIngredients == "ch":
		builder.addMushrooms()
	elif choosenIngredients == "pi":
		builder.addPeppers()
	elif choosenIngredients == "dq":
		builder.addDoubleCheese()
	elif choosenIngredients == "ac":
		builder.addOlive()
	elif choosenIngredients == "pp":
		builder.addPepperoni()
	elif choosenIngredients == "sa":
		builder.addSalami()
	elif choosenIngredients == "":
		return 1		
	else:
		print('ingrediente invalido')		
	return 0

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
		#print(colorama.Fore.RED + """
		#	Debe seleccionar el tamaño correcto!!""")
		#print(colorama.Style.RESET_ALL)
		seleccionar_tamaño()

def showIngredientsMenu():
	print("""
		SELECCIONE LOS INGREDIENTES
		Ingredientes:
		Jamón         (ja)
		Champiñones   (ch)
		Pimentón      (pi)
		Doble Queso   (dq)
		Aceitunas     (ac)
		Pepperoni     (pp)
		Salchichón    (sa)""")

def selectIngredients(builder):
	userResponse = ''

	print("""
		Indique el ingrediente (Pulse enter para terminar)""", end = ": ")
	userResponse = input()	
	correctIngredients = chooseIngredient(userResponse,builder)
	if(userResponse==""):
		return 0
	elif(correctIngredients==1):		
		#print(colorama.Fore.RED +""" 
		print("Debe seleccionar un ingrediente correcto!!")
		#print(colorama.Style.RESET_ALL)
		selectIngredients(builder)
	else:
		selectIngredients(builder)

def showAllTargetPizzaData(builder):
	#print("Usted selecciono una pizza "+ str(builder.getSize())+" con ")
	#print("Subtotal a pagar por una pizza "+builder.getSize()+" : " + builder.getPrice())
	print("*******************************************")

def getTotalPizzasPrice(pizzas):
	totalPrice = 0
	for pizza in pizzas:
		print(pizza)
		totalPrice += pizza.getPrice()
	return totalPrice


class main():	
	exit = False
	print_header()
	clientPizza = []

	while exit == False:
		pizza = Pizza()
		director = Kitchen()
		builder = ParticularPizzaBuilder(pizza)
		director.builder = builder
		clientPizza.append(pizza)
		
		print("""
			Pizza número """+ str(len(clientPizza)))
		seleccionar_tamaño()
		showIngredientsMenu()
		selectIngredients(builder)
		exit = selectAnotherPizza()
		showAllTargetPizzaData(builder)

	print("El pedido tiene un total de "+str(len(clientPizza))+" pizza(s) por un monto de "+str(getTotalPizzasPrice(clientPizza)))
	print("Gracias por su compra, regrese pronto")
