from player import Player
from bot import Bot
from character import Character
import random



class Battle:

    player = Player()
    bot = Bot

    def introduction(self):
        print(f"Bienvenidos a una pelea de pokemones entre:{self.player.character.name} vs ramon")

    def run(self):
        self.player.character.prepare_for_battle()
        self.player.character.attack()
        self.player.character.receive_damage()

    def show_winner(self):
        self.player.character.is_fainted


    def who_goes_first(self):
        players = [self.player , self.bot]
        first = random.choice(players)
        return first
