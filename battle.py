from player import Player
from bot import Bot
from character import Character
import random



class Battle:

    player = Player
    bot = Bot

    def introduction(self):
        print(f"Bienvenidos a una pelea de pokemones entre:{Player.character.name} vs ramon")

    def run(self):
        pass

    def show_winner(self):
        pass


    def who_goes_first(self):
        players = [self.player , self.bot]
        first = random.choice(players)
        return first
