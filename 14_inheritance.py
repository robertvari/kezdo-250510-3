import random

class Player_BASE:
    def __init__(self):
        self.my_number = 0

    def think_number(self):
        self.my_number = random.randint(1, 10)


class Player(Player_BASE):
    # partial method override
    def __init__(self):
        # runs BASE class __init__()
        super().__init__()
        self.name = "Csaba"
    
    # full method override
    def think_number(self):
        self.my_number = int(input("What is your guess? "))

class Computer(Player_BASE):
    pass

player = Player()
computer = Computer()

player.think_number()