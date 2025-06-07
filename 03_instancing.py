# class definition
class CoffeeMaker:
    model = None
    price = None
    color = None

class Person:
    name = None
    email = None

# instancing a class
philips = CoffeeMaker()
philips.model = "Philips"
philips.price = 24999
philips.color = "Silver"

sencor = CoffeeMaker()
sencor.model = "Sencor"
sencor.price = 12999
sencor.color = "Red"

csaba = Person()
csaba.name = "Kiss Csaba"
csaba.email = "csaba@gmail.com"

print(philips.model, philips.price, philips.color)
print(sencor.model, sencor.price, sencor.color)
print(csaba.name, csaba.email)