class CoffeeMaker:
    def __init__(self, model):
        self.model = model
        self.water = 100
        self.beans = 100
    
    def __str__(self):
        return f"{self.model} Water: {self.water} Beans: {self.beans}"

my_coffee_maker = CoffeeMaker("Sencor")
philips = CoffeeMaker("Philips")
print(my_coffee_maker)
print(philips)