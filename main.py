# AI-powered Text-based Adventure Game
import random
import time
#first run pip install colorama, then pip install termcolor
import colorama
from termcolor import colored

colorama.init()

class utils:
    @staticmethod
    def type_effect(str, interval=0.05, nextline=False, color="none"):
        for char in str:
            print(char, end='', flush=True)
            time.sleep(interval)
        if nextline:
            print()

class game:
    @staticmethod
    def start_game():
        utils.type_effect("AIventure: ")
        print("Version 1.0")

game.start_game()
