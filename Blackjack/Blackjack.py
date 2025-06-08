import os
from game_assets.cards import Deck
from game_assets.players import Player, AI_Player

class Blackjack:
    def __init__(self):
        self.intro()

        self.__reward = 10
        self.__deck = Deck()

        self.__players = [
            Player(),
            AI_Player(),
            AI_Player(),
            AI_Player()
        ]

        # start game
        self.game_loop()
    
    def game_loop(self):
        self.clear_screen()
        self.__deck.create()

        # init hands for all players
        for p in self.__players:
            p.init_hand(self.__deck)

        for p in self.__players:
            p.draw(self.__deck)
        
        self.get_winner()
    
    def get_winner(self):
        self.clear_screen()
        winner_list = []
        for p in self.__players:
            if p.hand_value <= 21:
                winner_list.append(p)

        if not winner_list:
            print("House wins")
        else:
            sorted_winners = sorted(winner_list, key=lambda p: p.hand_value)
            winner = sorted_winners[-1]
            print(f"The winner is: {winner.name}")
            winner.add_credits(self.__reward)

        if input("Do you want to play again? (y/n)") == "y":
            self.game_loop()
        else:
            print("Thanks for playing my game :)")

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