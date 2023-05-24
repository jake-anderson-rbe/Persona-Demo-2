import visual
import random
import sys
import testmap
import functions
from tkinter import *
import conversation
import profiles
import attendclass


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
    if profiles.Lana.level == 0:
      lanaintro()
    #if profiles.Lana.level >= 1:
      
  elif decide_input == "Attend Class":
    attendart()
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
    if profiles.Connor.level == 7:
      connorintro()
    #if profiles.Connor.level >= 8:
  elif decide_input == "Attend Class":
    attendmath()
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
    if profiles.Lana.level == 0:
      lanaintro()
    #if profiles.Lana.level >= 1:
  elif decide_input == "Attend Class":
    attendsocial()
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
    if profiles.Stephen.level == 3:
      stephenintro()
    #if profiles.Stephen.level >= 4:
  elif decide_input == "Attend Class":
    attendscience()
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
    if profiles.Connor.level == 7:
      connorintro()
    #if profiles.Connor.level >= 8:
  elif decide_input == "Attend Class":
    attendgym()
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
    if profiles.Sid.level == 15:
      sidintro()
    #if profiles.Sid.level >= 16:
  elif decide_input == "Attend Class":
    attendpool()
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
      if profiles.Sid.level == 15:
        sidintro()
      #if profiles.Sid.level >= 16:
        
    if characterchosen == "Lana":
      if profiles.Lana.level == 0:
        lanaintro()
      #if profiles.Lana.level >= 1:
  elif decide_input == "Attend Class":
    attendela()
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
      if profiles.Sid.level == 15:
        sidintro()
    if characterchosen == "Lana":
      if profiles.Lana.level == 0:
        lanaintro()
      #if profiles.Lana.level >= 1:

  elif decide_input == "Attend Class":
    attendclub()
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
      if profiles.stephen.level == 3:
        stephenintro()
      #if profiles.Lana.level >= 4:
    if characterchosen == "Connor":
      if profiles.connor.level == 7:
        connorintro()
      #if profiles.Lana.level >= 8:
  
  elif decide_input == "Attend Class":
    attendtrack()
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
print("Objective: Make Friends")
while True:
  travel()