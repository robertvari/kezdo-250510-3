import os, time, random

# compound class
class MagicNumber:
    def __init__(self):
        self.__player = Player()
        self.__computer = Computer()

    def start(self):
        self.clear_screen()

        print("-"*50, "MAGIC NUMBER", "-"*50)
        print(f"I think of a number between {self.__computer.min_number} and {self.__computer.max_number}. Can you guess it?")
        print(f"You start with {self.__player.credits} credits. If you win I give you 10 credit")
        print("If you lost all your credits the game ends.")

        input("Press Enter to continue...")

        self.game_loop()
    
    def game_loop(self):
        self.clear_screen()

        # classic python variable
        try_count = 3

        self.__computer.think_number()
        self.__player.think_number()

        while self.__computer.my_number != self.__player.my_number:
            try_count -= 1
            if try_count == 0:
                break
            self.clear_screen()
            print(f"Wrong guess. Try again. You have {try_count} tries left.")
            self.__player.think_number()
        
        self.clear_screen()

        # round end condition
        if self.__computer.my_number == self.__player.my_number:
            print("You win")
            self.__player.add_credits(10)
        else:
            print(f"You lost. {self.__computer.my_number} was my number")
            self.__player.take_credits(10)

        if self.__player.credits == 0:
            print("You lost all your credits. Game Over :((")
            self.exit_game()
        else:
            response = input("Do you want to play again? (y/n)")
            if response == "y":
                self.game_loop()
            else:
                self.exit_game()
    
    def exit_game(self):
        print("Thanks for playing my game")

    @staticmethod
    def clear_screen():
        os.system("cls")


class Player_BASE:
    def __init__(self):
        self.__my_number = 0
        self.__min_number = 1
        self.__max_number = 10
    
    def think_number(self):
        self.__my_number = 5

    @property
    def my_number(self):
        return self.__my_number
    
    @my_number.setter
    def my_number(self, new_number):
        self.__my_number = new_number
    
    @property
    def min_number(self):
        return self.__min_number
    
    @property
    def max_number(self):
        return self.__max_number


class Player(Player_BASE):
    def __init__(self):
        super().__init__()  # run BASE __init__()
        self.__credits = 10
    
    # override base
    def think_number(self):
        self.my_number = int(input("What is your guess? "))

    def add_credits(self, credits):
        self.__credits += credits
        print(f"You win {credits} credits. Now you have {self.__credits} cretids.")
    
    def take_credits(self, credits):
        self.__credits -= credits
        print(f"You lost {credits} credits. Now you left with {self.__credits} credits.")
    
    @property
    def credits(self):
        return self.__credits
    

class Computer(Player_BASE):
    pass


my_game = MagicNumber()
my_game.start()