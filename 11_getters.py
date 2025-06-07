class CoffeeMaker:
    def __init__(self, model, color, price):
        # private attributes
        self.__model = model
        self.__color = color
        self.__price = price
    
    def get_price(self):
        return self.__price
    
    def get_model(self):
        return self.__model
    
    def get_color(self):
        return self.__color
    
    def __str__(self):
        return f"Model: {self.__model}, Color: {self.__color}, Price: {self.__price}"

philips = CoffeeMaker("PHILIPS HD7411", "White", 12999)
print(philips.get_price(), philips.get_model(), philips.get_color())