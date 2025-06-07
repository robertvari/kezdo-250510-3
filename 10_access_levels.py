class CoffeeMaker:
    def __init__(self, model, color, price):
        # private attribute
        self.__model = model
        
        # protected attribute
        self._color = color

        # public attribute
        self.price = price
    
    def __str__(self):
        return f"Model: {self.__model}, Color: {self._color}, Price: {self.price}"

philips = CoffeeMaker("PHILIPS HD7411", "White", 12999)
philips.__model = "Csaba"
philips._color = "Red"
philips.price

print(philips)