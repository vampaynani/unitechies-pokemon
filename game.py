from battle import Battle
from catalog.pokemons import pokemones
class Game:
    user_name = " "
    battle = Battle()

    def ask_username(self):
        user_name = input("Cual es tu nombre?")

    def show_characters(self):
        print("Estos son los pokemos que puedes elegir: ")
        n = 1
        for pokemon in pokemones:
            print(f"{n}.{pokemon}")
            n += 1
    def ask_character(self):
        user_pokemon = input("Que pokemon eliges?")
        return user_pokemon


