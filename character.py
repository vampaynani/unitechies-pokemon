from catalog.pokemons import POKEMONS

class Character():
    name = " "
    health = 0
    speed = 0 
    defense = 0
    moves = " "

    def call_name(self):
        self.name = input().lower()
        return self.name 

    def call_health(self):
        self.health = POKEMONS[self.name]["hp"]
        return self.health