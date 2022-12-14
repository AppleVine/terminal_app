from os import system
from functions import * 
from classes import *

try:
    your_character = load_character()
except:
    pass
main_menu(your_character)