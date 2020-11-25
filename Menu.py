#import colorama
from datetime import datetime


#MENU (Texto)
def print_header():
	print("""
		Universidad Católica Andrés Bello
		Ingeniería Informática
		Programación en Python - Proyecto #1

		Integrantes del equipo:
		Luis Pinto - CI: 25.210.435
		Dexter Ramos - CI: 24.204.991
		José Andrés Rodríguez Pérez - CI: 27.663.836
		Ángel Sucasas - CI: 28.027.948
		
		*****************************
		*       PIZZERIA UCAB       *
		*****************************
		""")

#Menu para seleccionar el tamaño de la pizza (Texto)
def seleccionar_tamaño(builder):
    userResponse = ''

    print("""
        SELECCIONE EL TAMAÑO
        Opciones: Grande ( g ) -> [580], Mediana ( m ) -> [430], Personal ( p ) -> [280]""", end = ": ")
    userResponse = input()
    correctSize = chooseSize(userResponse, builder)
    if correctSize != 0:
        pass
    else:
		
    	#print(colorama.Fore.RED + """
          #  Debe seleccionar el tamaño correcto!!""")
    	#print(colorama.Style.RESET_ALL)
        seleccionar_tamaño(builder)


#Funcion para seleccionar el tamaño
def chooseSize(size, builder):
    if size == "g":
        builder.setSize("Grande")
        builder.setPrice(580)		
        return 1
    elif size == "m":
        builder.setSize("Mediana")		
        builder.setPrice(430)	
        return 1
    elif size == "p":
        builder.setSize("Personal")	
        builder.setPrice(280)		
        return 1		
    #else:
      	#print(colorama.Fore.RED + """
         #   Debe seleccionar el tamaño correcto!!""")
        #print(colorama.Style.RESET_ALL)	
        	
    return 0

#Menu de los ingredientes (Texto)
def showIngredientsMenu():
	print("""
		SELECCIONE LOS INGREDIENTES O PREFIERE UNA PIZZA DEL MENU
		Menu:
		Margarita		(ma)....................... 80 + coste del tamaño	-> jamon, doble queso
		Full House		(fh)....................... 303.5 + coste del tamaño	-> todos los ingredientes
		Champimenton		(cp)....................... 65 + coste del tamaño	-> champiñones, pimenton
		Vegetariana		(vg)....................... 122.5 + coste del tamaño	-> champiñones, pimenton, aceitunas
		Especial		(es)....................... 141 + coste del tamaño	-> jamon, pepperoni, salchichon
		Quesoroni		(qs)....................... 78.5 + coste del tamaño	-> doble queso, pepperoni

		Ingredientes:
		Jamón         (ja)....................... 40
		Champiñones   (ch)....................... 35
		Pimentón      (pi)....................... 30
		Doble Queso   (dq)....................... 40
		Aceitunas     (ac)....................... 57.5
		Pepperoni     (pp)....................... 38.5
		Salchichón    (sa)....................... 62.5 """)

#Menu para seleccionar los ingredientes (Texto)
def selectIngredients(builder):
	userResponse = ''

	print("""
		Indique la opcion (Pulse enter para terminar)""", end = ": ")
	userResponse = input()	
	if (userResponse == "ma"):
		correctIngredients = margarita(builder)
	elif userResponse == "fh":
		correctIngredients = fullhouse(builder)
	elif userResponse == "cp":
		correctIngredients = champimenton(builder)
	elif userResponse == "vg":
		correctIngredients = vegetariana(builder)
	elif userResponse == "es":
		correctIngredients = especial(builder)
	elif userResponse == "qs":
		correctIngredients = quesoroni(builder)
	else:
		correctIngredients = chooseIngredient(userResponse,builder)
	if(userResponse=="" and not len(builder.getPizza())):
		print("\n\t\tUsted ha seleccionado un pizza "+builder.getSize()+" Margarita")
		return 0
	elif(userResponse==""):
		print("\n\t\tUsted a seleccionado una pizza "+builder.getSize()+" con: ",end= '')
		builder.getIngre()
		return 0
	elif(correctIngredients==0):		
		#print(colorama.Fore.RED +""" 
		print("Debe seleccionar un ingrediente correcto!!")
		#print(colorama.Style.RESET_ALL)
		selectIngredients(builder)
	else:
		selectIngredients(builder)

#Funcion para seleccionar el ingrediente
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
	return 1

#Menu para agregar otra pizza 
def selectAnotherPizza():
	print("""
		¿Desea agregar otra pizza?[s/n]""", end = ": ")
	userResponse = input()
	if (userResponse == "s"):
		return False
	elif (userResponse == "S"):
		return False 
	elif (userResponse == "n"):
		return True
	elif (userResponse == "N"):
		return True  
	else:
		print('Respuesta invalida, intente otra vez')
		selectAnotherPizza()

#Funcion Decorativa
def showAllTargetPizzaData(builder):
	#print("Usted selecciono una pizza "+ str(builder.getSize())+" con ")
	#print("Subtotal a pagar por una pizza "+builder.getSize()+" : " + builder.getPrice())
	print("""
		*******************************************
		""")

#Funcion que calcula el precio de las pizza
def getTotalPizzasPrice(pizzas):
	totalPrice = 0
	for pizza in pizzas:
		print(pizza)
		totalPrice += pizza.getPrice()
	return totalPrice

#mostrar factura y guardar factura
def showReceipt(clientPizza):

	print(""" El pedido tiene un total de """ + str(len(clientPizza)) + """ pizza(s) """)
	
	print("""Usted ha ordenado: """)
	i=0
	archivo = open("factura.txt", "a")
	archivo.write(str(datetime.today()) + "\n")
	while i < len(clientPizza):
		x=clientPizza[i].getSize()
		y=clientPizza[i].list_parts
		z=clientPizza[i].getPrice()
		if is_empty(clientPizza[i].getIngredients()):
			print("Una pizza Margarita por un monto de " + str(z),end='')
			archivo.write("Una pizza Margarita por un monto de " + str(z) + "\n")
			print(",\n")
		else:
			print("Una pizza " +str(x)+ " con ",end= '')
			archivo.write("Una pizza " +str(x)+ " con " + str(listIngridients(clientPizza[i].getIngredients())))
			y()
			print(" por un monto de " + str(z),end='')
			archivo.write(" por un monto de " + str(z) + "\n")
			print(",\n")
		i+=1
	archivo.close()
#funcion que permite saber si una estructura esta vacia o no		
def is_empty(data_structure):
    if data_structure:
        return False
    else:
        return True



#Definicion de la pizza margarita
def margarita(builder):
	chooseIngredient("ja",builder)
	chooseIngredient("dq",builder)

#Definicion de la pizza fullhouse
def fullhouse(builder):
	chooseIngredient("ja",builder)
	chooseIngredient("dq",builder)
	chooseIngredient("ch",builder)
	chooseIngredient("ac",builder)
	chooseIngredient("pp",builder)
	chooseIngredient("sa",builder)
	chooseIngredient("pi",builder)

#Definicion de la pizza champimenton
def champimenton(builder):
	chooseIngredient("pi",builder)
	chooseIngredient("ch",builder)

#Definicion de la pizza vegetariana
def vegetariana(builder):
	chooseIngredient("pi",builder)
	chooseIngredient("ch",builder)
	chooseIngredient("ac",builder)

#Definicion de la pizza especial
def especial(builder):
	chooseIngredient("ja",builder)
	chooseIngredient("sa",builder)
	chooseIngredient("pp",builder)

#Definicion de la pizza quesoroni
def quesoroni(builder):
	chooseIngredient("dq",builder)
	chooseIngredient("pp",builder)

#Metodo para imprimir los elementos de una lista en este caso para el uso de guardar la factura
def listIngridients(list):	
	ingridients = ""
	for i in list:
		ingridients = ingridients + i + ", " 

	return ingridients