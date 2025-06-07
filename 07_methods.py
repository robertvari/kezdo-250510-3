import time, random

class CoffeeMaker:
    coffee_types = ["Espresso", "Doppio", "Latte", "Cappuccino"]
    
    def __init__(self, model):
        self.model = model
        self.water = 100
        self.beans = 100
        self.cofees_made = 0
    
    def display(self):
        print(f"Model: {self.model}, Water: {self.water}, Beans: {self.beans}, Coffees Made: {self.cofees_made}")

    def make_coffee(self):
        print("-"*10, self.model, "-"*10)
        for index, i in enumerate(self.coffee_types):
            print(index, i)

        coffe_number = int(input("Choose your coffee: "))

        print(f"Making a {self.coffee_types[coffe_number]}...")
        time.sleep(random.randint(3,6))
        print(f"Your {self.coffee_types[coffe_number]} is ready")
        print("Enjoy")

my_coffe_maker = CoffeeMaker("Sencor")
my_coffe_maker.make_coffee()