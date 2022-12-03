from catalog.pokemons import POKEMONS, pokemones, poderes
import random

class Bot:

    def initialize(self):
        """Selecciona un pokemon al azar"""
        bot_pokemon = pokemones[random.randint(0,5)]
        return bot_pokemon
    def select_move(self):
        """Selecciona un ataque al azar"""
        bot_attack = poderes[random.randint(0,6)]
        return bot_attack





