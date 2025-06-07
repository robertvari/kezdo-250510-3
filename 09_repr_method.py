class Person:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
    
    def __str__(self):
        return f"{self.name}, {self.email}, {self.address}"
    
    def __repr__(self):
        return self.name

csaba = Person("Kiss Csaba", "csaba@gmail.com", "Budapest")
tamas = Person("Nagy Tamás", "tamas@gmail.com", "Debrecen")

my_friends = [csaba, tamas]
print(my_friends)
print(csaba)