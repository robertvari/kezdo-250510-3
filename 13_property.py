class CoffeeMaker:
    def __init__(self, model, color, price):
        # private attributes
        self.__model = model
        self.__color = color
        self.__price = price
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        self.__price = new_price
    
    @property
    def color(self):
        return self.__color
    
    @property
    def model(self):
        return self.__model

philips = CoffeeMaker("PHILIPS HD7411", "White", 12999)
print(philips.price)
philips.price = 1000
print(philips.price)