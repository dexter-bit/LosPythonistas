class Pizza():	
	def __init__(self) -> None:
		self.ingridients=[]
		self.totalPrice=0
	
	def addIngridient(self, ingridient) -> None:
		self.ingridients.append(ingridient)

	def list_parts(self) -> None:
		print(f"pizza ingridients: {', '.join(self.ingridients)}", end="")
