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

class Customer:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
    
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

csaba = Customer("Kiss", "Csaba")
print(csaba.full_name)