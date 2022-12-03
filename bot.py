from catalog.pokemons import POKEMONS
import random
pokemones = ["bulbasaur", "charmander", "squirtle", "pikachu", "snorlax", "pidgeotto"]
poderes = ["tackle", "vine whip","fire punch", "water gun","thunder shock","mega punch","wing attack"]
class Bot:

    def initialize(self):
        """Selecciona un pokemon al azar"""
        bot_pokemon = pokemones[random.randint(0,5)]
        return bot_pokemon
    def select_move(self):
        """Selecciona un ataque al azar"""
        bot_attack = poderes[random.randint(0,6)]
        return bot_attack



bot = Bot()
print(bot.initialize())
print(bot.select_move())

