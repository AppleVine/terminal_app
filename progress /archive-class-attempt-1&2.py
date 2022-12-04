# class Wizard: 
#     def __init__(self, level = 0, cantrips_known = 0, level_1_spellslots = 0, level_2_spellslots = 0, level_3_spellslots = 0, level_4_spellslots = 0, level_5_spellslots = 0, level_6_spellslots = 0, level_7_spellslots = 0, level_8_spellslots = 0, level_9_spellslots = 0,):
#         self.level = level
#         self.cantrips_known = cantrips_known
#         self.level_1_spellslots = level_1_spellslots
#         self.level_2_spellslots = level_2_spellslots
#         self.level_3_spellslots = level_3_spellslots
#         self.level_4_spellslots = level_4_spellslots
#         self.level_5_spellslots = level_5_spellslots
#         self.level_6_spellslots = level_6_spellslots
#         self.level_7_spellslots = level_7_spellslots
#         self.level_8_spellslots = level_8_spellslots
#         self.level_9_spellslots = level_9_spellslots

# level_1_wizard = Wizard(1, 3, 2)
# level_2_wizard = Wizard(2, 3, 3)
# level_3_wizard = Wizard(3, 3, 4, 2)
# level_4_wizard = Wizard(4, 4, 4, 3)
# level_5_wizard = Wizard(5, 4, 4, 3, 2)
# level_6_wizard = Wizard(6, 4, 4, 3, 3)
# level_7_wizard = Wizard(7, 4, 4, 3, 3, 1)
# level_8_wizard = Wizard(8, 4, 4, 3, 3, 2)
# level_9_wizard = Wizard(9, 4, 4, 3, 3, 3, 1)
# level_10_wizard = Wizard(10, 5, 4, 3, 3, 3, 2)
# level_11_wizard = Wizard(11, 5, 4, 3, 3, 3, 2, 1)
# level_12_wizard = Wizard(12, 5, 4, 3, 3, 3, 2, 1)
# level_13_wizard = Wizard(13, 5, 4, 3, 3, 3, 2, 1, 1)
# level_14_wizard = Wizard(14, 5, 4, 3, 3, 3, 2, 1, 1)
# level_15_wizard = Wizard(15, 5, 4, 3, 3, 3, 2, 1, 1, 1)
# level_16_wizard = Wizard(16, 5, 4, 3, 3, 3, 2, 1, 1, 1)
# level_17_wizard = Wizard(17, 5, 4, 3, 3, 3, 2, 1, 1, 1, 1)
# level_18_wizard = Wizard(18, 5, 4, 3, 3, 3, 3, 1, 1, 1, 1)
# level_19_wizard = Wizard(19, 5, 4, 3, 3, 3, 3, 2, 1, 1, 1)
# level_20_wizard = Wizard(20, 5, 4, 3, 3, 3, 3, 2, 2, 1, 1)

# def write_character():
#     your_character = open("your_character.txt", "r+")
#     wizard_lines = ["Your wizard level is: ",   ]
#     your_character.close()





# your_wizard = Wizard(0,0)

# def get_spell_wizard():
#     input_level = 0
#     while input_level != "quit":
#         input_level = input("What level is your Wizard? ")
#         get_level = int(input_level)
#         if input_level == "quit":
#             quit()
#         elif get_level == 1:
#                 your_wizard = Wizard(1, 3, 2)
#                 your_character = open("your_character.txt", "r+")
#                 your_character.write("Your character is a Wizard.")
#                 your_character.write(str(your_wizard.level))
#                 your_character.close()
#                 break
#         elif get_level == 2:
#                 your_wizard = Wizard(2, 3, 3)
#                 return your_wizard
#         elif get_level == 3:
#                 your_wizard = Wizard(3, 3, 4, 2)
#                 return your_wizard
#         elif get_level == 4:
#                 your_wizard = Wizard(4, 4, 4, 3)
#                 return your_wizard
#         elif get_level == 5:
#                 your_wizard = Wizard(5, 4, 4, 3, 2)
#                 return your_wizard
#         elif get_level == 6:
#                 your_wizard = Wizard(6, 4, 4, 3, 3)
#                 return your_wizard
#         elif get_level == 7:
#                 your_wizard = Wizard(7, 4, 4, 3, 3, 1)
#                 return your_wizard
#         elif get_level == 8:
#                 your_wizard = Wizard(8, 4, 4, 3, 3, 2)
#                 return your_wizard
#         elif get_level == 9:
#                 your_wizard = Wizard(9, 4, 4, 3, 3, 3, 1)
#                 return your_wizard
#         elif get_level == 10:
#                 your_wizard = Wizard(10, 5, 4, 3, 3, 3, 2)
#                 return your_wizard
#         elif get_level == 11:
#                 your_wizard = Wizard(11, 5, 4, 3, 3, 3, 2, 1)
#                 return your_wizard
#         elif get_level == 12:
#                 your_wizard = Wizard(12, 5, 4, 3, 3, 3, 2, 1)
#                 return your_wizard
#         elif get_level == 13:
#                 your_wizard = Wizard(13, 5, 4, 3, 3, 3, 2, 1, 1)
#                 return your_wizard
#         elif get_level == 14:
#                 your_wizard = Wizard(14, 5, 4, 3, 3, 3, 2, 1, 1)
#                 return your_wizard
#         elif get_level == 15:
#                 your_wizard = Wizard(15, 5, 4, 3, 3, 3, 2, 1, 1, 1)
#                 return your_wizard
#         elif get_level == 16:
#                 your_wizard = Wizard(16, 5, 4, 3, 3, 3, 2, 1, 1, 1)
#                 return your_wizard
#         elif get_level == 17:
#                 your_wizard = Wizard(17, 5, 4, 3, 3, 3, 2, 1, 1, 1, 1)
#                 return your_wizard
#         elif get_level == 18:
#                 your_wizard = Wizard(18, 5, 4, 3, 3, 3, 3, 1, 1, 1, 1)
#                 return your_wizard
#         elif get_level == 19:
#                 your_wizard = Wizard(19, 5, 4, 3, 3, 3, 3, 2, 1, 1, 1)
#                 return your_wizard
#         elif get_level == 20:
#                 your_wizard = Wizard(20, 5, 4, 3, 3, 3, 3, 2, 2, 1, 1)
#                 return your_wizard
#         else:
#             print("That's not a valid option, please try again.")
#             input("Enter to continue.")
      



# get_spell_wizard()

