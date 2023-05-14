import visual
import testmap
from test import Character
from tkinter import *
#import test

test_dude = Character("Lil Dicky", "16", "Male", 23)

def dialogue_level_up():
  test_dude.level += 1

def dialogue_level_down():
  test_dude.level -= 1

def travel():
      print('"Alright, maybe another time!"')
      print("\nyou can go to:")
      for school_location in testmap.school_locations:
        print(school_location)
      movement_input = input("where do you go? ")
      print("\nyou can go to: ")
      if movement_input == "1st floor":
        for first_location in testmap.first_locations:
          print(first_location)
      elif movement_input == "2nd floor":
        for second_location in testmap.second_locations:
          print(second_location)

def dialogue_test():
    decide = input("a or b? ")
    if decide == "a":
      print("good choice")
      dialogue_level_up()
      print(test_dude.level)
    elif decide == "b":
      print("bad choice")
      dialogue_level_down()
      print(test_dude.level)


# Test Main
print("Welcome To School")
travel()
  print("< Lil Dicky >")
  print('"Hello [Basic Human Name Here], my name is Lil Dicky. Want to have a conversation?"')
  action_input = input("yes or no? > ")
  if action_input == "yes":
    if test_dude.level <= 24:
      dialogue_test()
      print("Test")
    else:
      print('"Oh, it seems we are already best friends. Why not go talk with the others?"')
    travel()
        
  elif action_input == "no":
    travel()