class CoffeeMaker:
    def __init__(self, model, color, price):
        # private attributes
        self.__model = model
        self.__color = color
        self.__price = price
        self.__valid_colors = ["White", "Green", "Red", "Blue"]
    
    def get_price(self):
        return self.__price
    
    def get_valid_colors(self):
        return tuple(self.__valid_colors)
    
    def set_price(self, new_price):
        assert isinstance(new_price, int), "Price must be of type int"
        assert new_price > 5000, "Price is to low. It must be greater than 5000"
        self.__price = new_price
    
    def get_model(self):
        return self.__model
    
    def get_color(self):
        return self.__color
    
    def set_color(self, new_color):
        assert isinstance(new_color, str), "Color must be of type str"
        assert new_color in self.__valid_colors, f"These are the suported colors: {self.__valid_colors}"
        self.__color = new_color
    
    def __str__(self):
        return f"Model: {self.__model}, Color: {self.__color}, Price: {self.__price}"

philips = CoffeeMaker("PHILIPS HD7411", "White", 12999)