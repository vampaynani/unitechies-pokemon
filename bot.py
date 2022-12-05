from catalog.pokemons import POKEMONS
from catalog.moves import MOVES
import random

class Bot:

    def initalize(self):
        bot_pokemon = POKEMONS[random.randint(0,5)]["name"]
        return bot_pokemon
    
    def select_move(self):
        """Selecciona un ataque al azar"""
        bot_attack = MOVES[random.randint(0,6)]["power"]
        return bot_attack


bot = Bot()
print(bot.initalize())
print(bot.select_move())





