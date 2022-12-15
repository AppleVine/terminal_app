from classes import * 
from functions import *
import pytest


def test_class_selector_Datatype():
    with pytest.raises(Exception):
        class_selector("Wizard")

def test_class_selector_nodata():
    with pytest.raises(Exception):
        class_selector()

def test_main_menu_DataType():
    main_menu_selection = 25
    with pytest.raises(Exception):
        main_menu()
    


# We need your_character to of one of the two classes to work. Testing to make sure it has the data available (especially when loading in). 

def test_get_spells():
    your_character = None
    with pytest.raises(Exception):
        get_spells(your_character)
    
