import colorama

#MENU (Texto)
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

#Menu para seleccionar el tamaño de la pizza (Texto)
def seleccionar_tamaño(builder):
    userResponse = ''

    print("""
        SELECCIONE EL TAMAÑO
        Opciones: Grande ( g ) Mediana ( m ) Personal ( p )""", end = ": ")
    userResponse = input()
    correctSize = chooseSize(userResponse, builder)
    if correctSize != 0:
        pass
    else:
        print(colorama.Fore.RED + """
            Debe seleccionar el tamaño correcto!!""")
        print(colorama.Style.RESET_ALL)
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
    else:
        print(colorama.Fore.RED + """
            Debe seleccionar el tamaño correcto!!""")
        print(colorama.Style.RESET_ALL)		
    return 0

#Menu de los ingredientes (Texto)
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

#Menu para seleccionar los ingredientes (Texto)
def selectIngredients(builder):
	userResponse = ''

	print("""
		Indique el ingrediente (Pulse enter para terminar)""", end = ": ")
	userResponse = input()	
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