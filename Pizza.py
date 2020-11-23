class Pizza():  
    def __init__(self) -> None:
        self.ingredients = []
        self.totalPrice = 0
        self.size = "" 
    
    def addIngredient(self, ingredient):
        self.ingredients.append(ingredient)

    def addSize(self, size):
        self.size = size

    def addPrice(self, price):
        self.totalPrice = price

    def list_parts(self) -> None:
        print(f"pizza ingridients: {', '.join(self.ingredients)}", end="")

    def getPizzaSize(self) -> None:
        print(self.size)