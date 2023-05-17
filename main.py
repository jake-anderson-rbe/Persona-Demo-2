import visual
import random
import sys
import testmap
import functions
from test import Character
from tkinter import *
import conversation
from conversation import lanaone
from conversation import lanatwo
from conversation import lanathree
 # Defs
Rooms = ("Talk", "Attend Class", "Leave")

#def dialogue_level_up():
  #test_dude.level += 1
#def dialogue_level_down():
  #test_dude.level -= 1


def art():
  print(f"\n{testmap.Art.discription}")
  print(f"You see {testmap.Art.character}")
  for decide in Rooms:
    print(f"{decide}")
  decide_input = input("\nWhat do you do?:")
  if decide_input == "Talk":
    result = random.randint(1, 1)
    if result == 1:
      lanaone()
    if result == 2:
      lanatwo()
    if result == 3:
      lanathree()
  #elif decide_input == "Attend Class":
    #classes()
  elif decide_input == "Leave":
    travel()
def math():
  print(f"{testmap.Math.discription}")
  print(f"You see {testmap.Math.character}")
def social():
  print(f"{testmap.Social.discription}")
  print(f"You see {testmap.Social.character}")
def science():
  print(f"{testmap.Science.discription}")
  print(f"You see {testmap.Science.character}")
def ela():
  print(f"{testmap.ELA.discription}")
  print(f"You see {testmap.ELA.character}")


def travel():
      print("\nyou can go to:")
      for school_location in testmap.school_locations:
        print(school_location)
      movement_input = input("where do you go? ")
      print("\nyou can go to: ")
      if movement_input == "1st floor":
        for first_location in testmap.first_locations:
          print(first_location)
        movement_input = input("where do you go? ")
        if movement_input == "Math":
          math()
        if movement_input == "Social":
          social()
        if movement_input == "Art":
          art()

      if movement_input == "2nd floor":
        for first_location in testmap.first_locations:
          print(first_location)
        movement_input = input("where do you go? ")
        if movement_input == "ELA":
          ela()
        if movement_input == "Science":
          science()




# Test Main
print("Welcome to School")
travel()