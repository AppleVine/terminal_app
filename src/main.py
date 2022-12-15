from os import system
from functions import * 
from classes import *



try:
    your_character = load_character()
except FileNotFoundError:
    input("Save file is not found. Please create a character.\nPress Enter to continue.\n\n-------- \n\n")
main_menu(your_character)