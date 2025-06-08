import os

class Blackjack:
    def __init__(self):
        self.intro()

    def intro(self):
        self.clear_screen()
        print("-"*50, "BLACKJACK", "-"*50)
        print("Wellcome to Blackjack!")
        print("Get as close to 21 as possible without going over. Beat the others.")
        print("If your hand is higher than the others without going over 21 → You win.")

        input("Press Enter to continue...")

    def exit_game(self):
        pass

    def clear_screen(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

Blackjack()