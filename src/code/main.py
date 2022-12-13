from os import system
from functions import * 
from classes import *


your_character = Full_Caster("Wizard", 0)

try:
    load_character()
except:
    pass
main_menu()