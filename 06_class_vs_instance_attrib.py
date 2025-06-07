class CoffeeMaker:
    # class attribute
    use_electricity = True
    
    def __init__(self, model):
        # instance attribute
        self.model = model


philips = CoffeeMaker("Philips")
sencor = CoffeeMaker("Sencor")
CoffeeMaker.use_electricity = False

print(philips.model, philips.use_electricity)
print(sencor.model, sencor.use_electricity)