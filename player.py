from catalog.moves import MOVES
import random
from character import Character
character = Character()

class Player():
    name = " "
    character = Character()

    def select_move(self):
        """Selecciona un ataque al azar"""
        bot_attack = MOVES[random.randint(0,6)]["power"]
        return bot_attack
