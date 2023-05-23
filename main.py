import visual
import random
import sys
import testmap
import functions
from tkinter import *
import conversation



 # Defs
#Rooms = ("Talk", "Attend Class", "Leave")



# Art Class
def art():
  print(f"\n{testmap.Art.discription}")
  print(f"You see {testmap.Art.character} painting in a corner.")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input == "Talk":
    result = random.randint(1, 3)
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
    
# Math Class
def math():
  print(f"{testmap.Math.discription}")
  print(f"You see {testmap.Math.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input == "Talk":
    result = random.randint(1, 3)
    if result == 1:
      connorone()
    if result == 2:
      connortwo()
    if result == 3:
      connorthree()
  #elif decide_input == "Attend Class":
    #classes()
  elif decide_input == "Leave":
    travel()
    
# Social Class
def social():
  print(f"{testmap.Social.discription}")
  print(f"You see {testmap.Social.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input == "Talk":
    result = random.randint(1, 3)
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

# Science Class
def science():
  print(f"{testmap.Science.discription}")
  print(f"You see {testmap.Science.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input == "Talk":
    result = random.randint(1, 3)
    if result == 1:
      stephenone()
    if result == 2:
      stephentwo()
    if result == 3:
      stephenthree()
  #elif decide_input == "Attend Class":
    #classes()
  elif decide_input == "Leave":
    travel()

# Gym Class
def gym():
  print(f"{testmap.Gym.discription}")
  print(f"You see {testmap.Gym.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input == "Talk":
    result = random.randint(1, 3)
    if result == 1:
      connorone()
    if result == 2:
      connortwo()
    if result == 3:
      connorthree()
  #elif decide_input == "Attend Class":
    #classes()
  elif decide_input == "Leave":
    travel()
    
# pool Class
def pool():
  print(f"{testmap.Pool.discription}")
  print(f"You see {testmap.Pool.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input == "Talk":
    result = random.randint(1, 3)
    if result == 1:
      sidone()
    if result == 2:
      sidtwo()
    if result == 3:
      sidthree()
  #elif decide_input == "Attend Class":
    #classes()
  elif decide_input == "Leave":
    travel()

# ELA Class
def ela():
  print(f"{testmap.ELA.discription}")
  print(f"You see {testmap.ELA.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input == "Talk":
    characterchosen = input("Who do you want to talk to? :")
    if characterchosen == "Sid":
      result = random.randint(1, 3)
      if result == 1:
        sidone()
      if result == 2:
        sidtwo()
      if result == 3:
        sidthree()
    if characterchosen == "Lana":
      result = random.randint(1, 3)
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

# Club Building Class
def club():
  print(f"{testmap.Club.discription}")
  print(f"You see {testmap.Club.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input == "Talk":
    characterchosen = input("Who do you want to talk to? :")
    if characterchosen == "Sid":
      result = random.randint(1, 3)
      if result == 1:
        sidone()
      if result == 2:
        sidtwo()
      if result == 3:
        sidthree()
    if characterchosen == "Lana":
      result = random.randint(1, 3)
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

# Track Class
def track():
  print(f"{testmap.Track.discription}")
  print(f"You see {testmap.Track.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input == "Talk":
    characterchosen = input("Who do you want to talk to? :")
    if characterchosen == "Stephen":
      result = random.randint(1, 3)
      if result == 1:
        stephenone()
      if result == 2:
        stephentwo()
      if result == 3:
        stephenthree()
    if characterchosen == "Connor":
      result = random.randint(1, 3)
      if result == 1:
        connorone()
      if result == 2:
        connortwo()
      if result == 3:
        connorthree()
  #elif decide_input == "Attend Class":
    #classes()
  elif decide_input == "Leave":
    travel()



#System for getting around
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
        for second_location in testmap.second_locations:
          print(second_location)
        movement_input = input("where do you go? ")
        if movement_input == "ELA":
          ela()
        if movement_input == "Science":
          science()

      if movement_input == "Yard":
        for yard_location in testmap.yard_locations:
          print(yard_location)
        movement_input = input("where do you go? ")
        if movement_input == "Gym":
          gym()
        if movement_input == "Club Building":
          club()
        if movement_input == "Pool":
          pool()
        if movement_input == "Track Field":
          track()



# Test Main
print("Welcome to School")
while True:
  travel()