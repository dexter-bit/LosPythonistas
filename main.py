from Kitchen import Kitchen
from ParticularPizzaBuilder import ParticularPizzaBuilder
from Pizza import Pizza
from PizzaBuilder import PizzaBuilder

from abc import ABC, abstractmethod, abstractproperty
import colorama

def print_header():
	print("""
		Universidad Católica Andrés Bello
		Ingeniería Informática
		Programación en Python - Proyecto #1

		Integrantes del equipo:
		Luis Pinto - CI:
		Dexter Ramos - CI:
		José Andrés Rodríguez Pérez - CI: 27.663.836
		Ángel Sucasas - CI: 
		
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


def seleccionar_ingredientes():
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

	if userResponse == 'ja' or userResponse == 'ch' or userResponse == 'pi' or userResponse == 'dq' or userResponse == 'ac' or userResponse == 'pp' or userResponse == 'sa':
		print("Desea seleccionar otro ingrediente? \n\n Para agregar escriba *si* para declinar escriba *no*")
		userResponse = input()
		if 	userResponse == 'si' :
			seleccionar_ingredientes()
		elif userResponse == 'no':
			return 0
	else:
		print(colorama.Fore.RED + """
			Debe seleccionar un ingrediente correcto!!""")
		print(colorama.Style.RESET_ALL)
		seleccionar_ingredientes()


class main():
	director = Kitchen()
	builder = ParticularPizzaBuilder()
	director.builder = builder

	exit = False

	while exit == False:
		print_header()
		seleccionar_tamaño()
		seleccionar_ingredientes()
		