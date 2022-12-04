from catalog.pokemons import POKEMONS
from game import Game
pokemon = Game()
user_poke = pokemon.ask_character


class Character:
    name = " "
    health = 0
    speed = 0 
    defense = 0
    moves = " "

    def call_name(self):
        self.name = input().lower()
        return self.name 

    def prepare_for_battle():
        pass

    def is_fainted():
        pass

    def attack(pokemon):
        pass

    def receive_damage():
        pass 





    # def call_health(self):
    #     self.health = POKEMONS[self.name]["hp"]
    #     return self.health
    
    # def call_speed(self):
    #     self.speed = POKEMONS[self.speed]["speed"]
    #     return self.speed

    # def call_defense(self):
    #     self.defense = POKEMONS[self.defense]["defense"]
    #     return self.defense    

    # def call_moves(self):
    #     self.moves = input().lower()
    #     return self.moves

pokemon = Character()

print(pokemon.call_name())