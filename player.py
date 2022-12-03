from game import Game

user = Game()

class Player(user.ask_username, user.ask_character):
    player = " "
    character = " "

    def select_move(self):
        pass
