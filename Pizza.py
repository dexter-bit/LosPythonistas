class Pizza():	
	def __init__(self) -> None:
		self.ingredients = []
		self.totalPrice = 0
		self.size = "" 
	
	def addIngredient(self, ingridient) -> None:
		self.ingredients.append(ingridient)

	def list_parts(self) -> None:
		print(f"pizza ingridients: {', '.join(self.ingridients)}", end="")
