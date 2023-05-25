import visual
import random
import sys
import testmap
import functions
from tkinter import *
import conversation
import profiles

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
    if profiles.Lana.level >= 1:
      lanaconvo()
      
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
    if profiles.Connor.level >= 8:
      connorconvo()
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
    if profiles.Lana.level >= 1:
      lanaconvo()
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
    if profiles.Stephen.level >= 4:
      stephenconvo()
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
    if profiles.Connor.level >= 8:
      connorconvo()
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
    if profiles.Sid.level >= 16:
      sidconvo()
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
      if profiles.Sid.level >= 16:
        sidconvo()
    if characterchosen == "Lana":
      if profiles.Lana.level == 0:
        lanaintro()
      if profiles.Lana.level >= 1:
        lanaconvo()
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
      if profiles.Sid.level >= 1:
        sidconvo()
    if characterchosen == "Lana":
      if profiles.Lana.level == 0:
        lanaintro()
      if profiles.Lana.level >= 1:
        lanaconvo()
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
      if profiles.Stephen.level >= 4:
        stephenconvo()
    if characterchosen == "Connor":
      if profiles.connor.level == 7:
        connorintro()
      if profiles.Connor.level >= 8:
        connorconvo()
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
      if movement_input == "1st floor":
        print("\nyou can go to:")
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
        print("\nyou can go to:")
        for second_location in testmap.second_locations:
          print(second_location)
        movement_input = input("where do you go? ")
        if movement_input == "ELA":
          ela()
        if movement_input == "Science":
          science()

      if movement_input == "Yard":
        print("\nyou can go to:")
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

      else:
        print("You end up back at the entrance.")


def attendart():
  profiles.Lana.level += 2
  print("""By showing interest in Lana's favorite class, you grew closer. 
  [Relationship Increased By 2]""")
def attendsocial():
  profiles.Lana.level += 1
  print("""Though reluctant to accept your help, Lana learned from you.
  [Relationship Increased By 1]""")
def attendscience():
  profiles.Stephen.level += 0
  print(""""You try to spend time with Stephen but he is too busy with a personal experiment.
  [Relationship Did Not Increase]""")
def attendela():
  profiles.Lana.level += 1
  profiles.Sid.level += 4
  print("""You and Sid convinced Lana to join you for a short homework session after class.
  [Lana Relationship Increaded By 1]
  [Sid Relationship Increased By 4]""")
def attendgym():
  profiles.Connor.level += 2
  print("""You, Connor and a few other students play basketball.
  Luckily you were on a team with Connor.
  You and Connor dominated the court.
  [Relationship with Connor Increased By 2]""")
def attendpool():
  profiles.Sid.level += 2
  print("""You and Sid have a few races in the pool.
  He beat you 4 - 0.
  [Relationship Increased By 2]
  [Pride Decreased By 999]
  """)
def attendtrack():
  profiles.Connor.level += 5
  profiles.Stephen.level -= 2
  print("""You and Connor try to cheer Stephen on as he runs around the track.
  Connor and you had fun but Stephen was to exhausted to even talk.
  [Stephen Relationship Decreased By 2]
  [Connor Relationship Increased By 5]""")
def attendmath():
  profiles.Connor.level += 3
  print("""Connor, to your surprise, was intensly listening to the lesson.
  By helping him with the parts he didint understand, you grew closer.
  [Relatinship Increased By 3""")
def attendclub():
  profiles.Sid.level -= 4
  profiles.Lana.level += 2
  print("""Sid sat bored out of his mind while you and Lana help the drama club paint posters for the upcoming play.
  [Relationship With Sid Decreased By 4]
  [Relationship With Lana Increased By 2]""")

def tutorial():
  print("\nYour old friend Sid approaches you")
  tutorialinput = input("Do you want to talk with him? (Yes) (No):")
  if tutorialinput == "Yes":
    print("You go to meet Sid")


  if tutorialinput == "No":
    travel()
    
# Test Main
print("Welcome to HighSchool")
print("You just transfered here as a 2nd year and know nobody here.")
print("Except your best friend from elementary, Sid.")
print("""But one friend isnt enough to get you through this battleground. 
so why not go out and make some more""")
print("\nObjective: Make Friends")

tutorial()


while True:
  travel()