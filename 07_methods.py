class CoffeeMaker:
    coffee_types = ["Espresso", "Doppio", "Latte", "Cappuccino"]
    
    def __init__(self, model):
        self.model = model
        self.water = 100
        self.beans = 100
        self.cofees_made = 0
    
    def display(self):
        print(f"Model: {self.model}, Water: {self.water}, Beans: {self.beans}, Coffees Made: {self.cofees_made}")


my_coffe_maker = CoffeeMaker("Sencor")
my_coffe_maker.display()