from battle import Battle
from catalog.pokemons import POKEMONS
from player import Player
from character import Character
player = Player()


class Game:
    user_name = " "
    battle = Battle()

    def ask_username(self):
        user_name = input("Cual es tu nombre? ")
        return user_name

    def show_characters(self):
        print("Estos son los pokemos que puedes elegir: ")
        for i in range(0,5):
            print(f'{i+1}.{POKEMONS[i]["name"]}')
            
    def ask_character(self):
        user_pokemon = input("Que pokemon eliges? ").lower()
        player.character = user_pokemon 
        

    def setup_player(self):
        player = Player()
        player.name = self.user_name
        
        
    def setup_bot(self):
        pass

    def setup_battle(self):
        battle = Battle()
        battle.introduction()




