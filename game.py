from battle import Battle
from catalog.pokemons import pokemones
class Game:
    user_name = " "
    battle = Battle()

    def ask_username(self):
        user_name = input("Cual es tu nombre?")

    def show_characters(self):
        print(f"Estos son los pokemones disponibles: {pokemones}")

