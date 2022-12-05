from battle import Battle
from catalog.pokemons import POKEMONS


class Game:
    user_name = " "
    battle = Battle()

    def ask_username(self):
        user_name = input("Cual es tu nombre?")
        return user_name

    def show_characters(self):
        print("Estos son los pokemos que puedes elegir: ")
        n = 1
        for i in range(0,5):
            print(f'{n}.{POKEMONS[i]["name"]}')
            n += 1
    def ask_character(self):
        user_pokemon = input("Que pokemon eliges?")
        return user_pokemon

    def setup_player(self, ask_username):
        name = " "




