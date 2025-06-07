class CoffeeMaker:
    def __init__(self, model, price, color):
        # instance attribute
        self.model = model
        self.price = price
        self.color = color

philips = CoffeeMaker("Philips", 19999, "Red")
sencor = CoffeeMaker("Sencor", 12999, "Silver")

print(philips.model, philips.color, philips.price)
print(sencor.model, sencor.color, sencor.price)