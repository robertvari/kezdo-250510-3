class CoffeeMaker:
    def __init__(self, model, color, price):
        # private attribute
        self.__model = model
        
        # protected attribute
        self.__color = color

        # public attribute
        self.__price = price
    
    def __str__(self):
        return f"Model: {self.__model}, Color: {self.__color}, Price: {self.__price}"

philips = CoffeeMaker("PHILIPS HD7411", "White", 12999)
philips.__model = "Csaba"
philips.__color = "Red"
philips.__price = 8999

print(philips)