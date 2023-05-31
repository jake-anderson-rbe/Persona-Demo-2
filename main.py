import random
import intros
import sys
import map
from tkinter import *
import conversation
import profiles
import textwrap

dayvalue = 0
timevalue = 0
timeuntilend = 6
actionsleft = 3
maxrelation = 25

# Art Class
def art():
  print(f"\n{map.Art.discription}")
  print("You spot someone painting in the corner.")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input == "Talk":
      intros.lanaintro_1()
      if profiles.Lana.level >= 1:
        conversation.lanaconvo()
      elif profiles.Lana.level >= 25:
        print("You Already Reached Max Relationship Level With This Person")    
  elif decide_input == "Attend Class":
    attendart1()
    if profiles.Lana.level >= 1:
      attendart2()
  elif decide_input == "Leave":
    travel()
    
# Math Class
def math():
  print(f"{map.Math.discription}")
  print(f"You see {map.Math.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input == "Talk":
    if profiles.Connor.level == 7:
      connorintro()
    elif profiles.Connor.level >= 8:
      connorconvo()
    elif profiles.Connor.level >= 25:
      print("You Already Reached Max Relationship Level With This Person")
  elif decide_input == "Attend Class":
    attendmath()
  elif decide_input == "Leave":
    travel()
    
# Social Class
def social():
  print(f"{map.Social.discription}")
  print(f"You see {map.Social.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input == "Talk":
    if profiles.Lana.intro == 1:
      conversation.lanaconvo()
    elif profiles.Lana.level >= 25:
      print("You Already Reached Max Relationship Level With This Person")
    elif profiles.Lana.intro == 0:
      print(textwrap.dedent("""She seems wary of you. 
Maybe talk to her when she is in a place more familiar to her."""))
  elif decide_input == "Attend Class":
    attendsocial()
  elif decide_input == "Leave":
    travel()

# Science Class
def science():
  print(f"{map.Science.discription}")
  print(f"You see {map.Science.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input == "Talk":
    if profiles.Stephen.level == 3:
      stephenintro()
    elif profiles.Stephen.level >= 4:
      stephenconvo()
    elif profiles.Stephen.level >= 25:
      print("You Already Reached Max Relationship Level With This Person")
  elif decide_input == "Attend Class":
    attendscience()
  elif decide_input == "Leave":
    travel()

# Gym Class
def gym():
  print(f"{map.Gym.discription}")
  print(f"You see {map.Gym.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input == "Talk":
    if profiles.Connor.level == 7:
      connorintro()
    elif profiles.Connor.level >= 8:
      connorconvo()
    elif profiles.Connor.level >= 25:
      print("You Already Reached Max Relationship Level With This Person")
  elif decide_input == "Attend Class":
    attendgym()
  elif decide_input == "Leave":
    travel()
    
# pool Class
def pool():
  print(f"{map.Pool.discription}")
  print(f"You see {map.Pool.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input == "Talk":
    if profiles.Lana.level == 15:
      sidintro()
    elif profiles.Lana.level >= 16:
      sidconvo()
    elif profiles.Lana.level >= 25:
      print("You Already Reached Max Relationship Level With This Person")
  elif decide_input == "Attend Class":
    attendpool()
  elif decide_input == "Leave":
    travel()

# ELA Class
def ela():
  print(f"{map.ELA.discription}")
  print(f"You see {map.ELA.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input == "Talk":
    characterchosen = input("Who do you want to talk to? :")
    if characterchosen == "Sid":
      if profiles.Sid.level == 15:
        sidintro()
      elif profiles.Sid.level >= 16:
        sidconvo()
      elif profiles.Sid.level >= 25:
        print("You Already Reached Max Relationship Level With This Person")
    if characterchosen == "Lana":
      if profiles.Lana.level == 0:
        lanaintro()
      elif profiles.Lana.level >= 1:
        lanaconvo()
      elif profiles.Lana.level >= 25:
        print("You Already Reached Max Relationship Level With This Person")
  elif decide_input == "Attend Class":
    attendela()
  elif decide_input == "Leave":
    travel()

# Club Building Class
def club():
  print(f"{map.Club.discription}")
  print(f"You see {map.Club.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input == "Talk":
    characterchosen = input("Who do you want to talk to? :")
    if characterchosen == "Sid":
      if profiles.Sid.level == 15:
        sidintro()
      elif profiles.Sid.level >= 1:
        sidconvo()
      elif profiles.Sid.level >= 25:
        print("You Already Reached Max Relationship Level With This Person")        
    if characterchosen == "Lana":
      if profiles.Lana.level == 0:
        lanaintro()
      elif profiles.Lana.level >= 1:
        lanaconvo()
      elif profiles.Lana.level >= 25:
        print("You Already Reached Max Relationship Level With This Person")
  elif decide_input == "Attend Class":
    attendclub()
  elif decide_input == "Leave":
    travel()

# Track Class
def track():
  print(f"{map.Track.discription}")
  print(f"You see {map.Track.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input == "Talk":
    characterchosen = input("Who do you want to talk to? :")
    if characterchosen == "Stephen":
      if profiles.stephen.level == 3:
        stephenintro()
      elif profiles.Stephen.level >= 4:
        stephenconvo()
      elif profiles.Stephen.level >= 25:
        print("You Already Reached Max Relationship Level With This Person")
    if characterchosen == "Connor":
      if profiles.connor.level == 7:
        connorintro()
      elif profiles.Connor.level >= 8:
        connorconvo()
      elif profiles.Connor.level >= 25:
        print("You Already Reached Max Relationship Level With This Person")
  elif decide_input == "Attend Class":
    attendtrack()
  elif decide_input == "Leave":
    travel()


#System for getting around
def travel():
  print("\nyou can go to:")
  for school_location in map.school_locations:
    print(school_location)
  movement_input = input("where do you go? ")
  if movement_input == "1st Floor":
    print("\nyou can go to:")
    for first_location in map.first_locations:
      print(first_location)

    movement_input = input("where do you go? ")
    if movement_input == "Math":
      math()
    if movement_input == "Social":
      social()
    if movement_input == "Art":
      art()

  elif movement_input == "2nd Floor":
    print("\nyou can go to:")
    for second_location in map.second_locations:
      print(second_location)
    movement_input = input("where do you go? ")
    if movement_input == "ELA":
      ela()
    if movement_input == "Science":
      science()

  elif movement_input == "Yard":
    print("\nyou can go to:")
    for yard_location in map.yard_locations:
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

  elif movement_input == "Check Relationships":
    print(f"{profiles.Lana.name}, {profiles.Lana.level}")
    print(f"{profiles.Lana.name}, {profiles.Lana.level}")

  elif movement_input == "debug":
    conversation.lanaintro()

  elif movement_input == "debug 2":
    print("lana intro complete")
    profiles.Lana.intro += 1
  
  else:
    print("You end up back at the entrance.")
    travel()


# Classes
def attendart():
  if conversation.lanaIntroEnd.complete == 0:
    print("You attend the class.")
  if conversation.lanaIntroEnd.complete == 1:
    profiles.Lana.level += 2
    maxrelation += 2
    print("""By showing interest in Lana's favorite class, you grew closer. 
            [Relationship Increased By 2]""")
def attendsocial():
  if conversation.lanaIntroEnd.complete == 0:
    print("You attend the class.")
  if conversation.lanaIntroEnd.complete == 1:
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
  maxrelation += 5
  print("""You and Sid convinced Lana to join you for a short homework session after class.
            [Lana Relationship Increaded By 1]
            [Sid Relationship Increased By 4]""")
def attendgym():
  profiles.Connor.level += 2
  maxrelation += 2
  print(textwrap.dedent("""You, Connor and a few other students play basketball.
Luckily you were on a team with Connor.
You and Connor dominated the court.
            [Relationship with Connor Increased By 2]"""))
def attendpool():
  profiles.Lana.level += 2
  maxrelation += 2
  print("""You and Sid have a few races in the pool.
He beat you 4 - 0.
            [Relationship Increased By 2]
            [Pride Decreased By 999]
  """)
def attendtrack():
  profiles.Connor.level += 5
  profiles.Stephen.level -= 2
  maxrelation += 3
  print("""You and Connor try to cheer Stephen on as he runs around the track.
Connor and you had fun but Stephen was to exhausted to even talk.
            [Stephen Relationship Decreased By 2]
            [Connor Relationship Increased By 5]""")
def attendmath():
  profiles.Connor.level += 3
  maxrelation += 3
  print("""Connor, to your surprise, was intensly listening to the lesson.
By helping him with the parts he didint understand, you grew closer.
            [Relatinship Increased By 3""")
def attendclub():
  profiles.Lana.level -= 4
  profiles.Lana.level += 2
  maxrelation -= 2
  print("""Sid sat bored out of his mind while you and Lana help the drama club paint posters for the upcoming play.
            [Relationship With Sid Decreased By 4]
            [Relationship With Lana Increased By 2]""")


# Tutorial
def tutorial():
  print("\nYour old friend Sid approaches you\n")
  tutorialinput = input("Do you want to talk with him? (Yes) (No):")
  if tutorialinput == "Yes":
    print("You go to meet Sid")
    conversation.sidintro()
    print("""\nYou bid Sid goodbye and enter the school.
You enter the first class you see, art class.""")
    art()
    print("""\nThe Bell signalling the end of class goes and you swiftly exit.
You get swept up in the crowd of kids.
Next thing you know, you are in a Gym""")
    gym()
    print("""\nYou and Connor walk to the main building.
The moment you two enter, you are once again taken by a crowd.
you reach for Connors hand in the sea of students, but he is already gone.
Instead you grab hold of a... textbook!?
Welcome to math class.""")
    math()
    print("""\nFor the last time, you are swept up in a crowd as you exit class.
You find yourself at the entrance of the school.
Finally, you get some time to yourself.
Time to officially start your school life!""")
  
    
  if tutorialinput == "No":
    print("\nYou spend the day wandering the halls")



# Test Main
print("Welcome to HighSchool")
print("You just transfered here as a 2nd year and know nobody here.")
print("Except your best friend from elementary, Sid.")
print("""But one friend isnt enough to get you through this battleground. 
so why not go out and make some more""")
print("\nObjective: Meet Fellow Students ")

tutorial()
timevalue += 3
actionsleft -= 3

if timevalue == 3:
  timeuntilend -= 1
  print(f"""\nAfter a busy day at school, 
it seems time to head home.\n
You wake up the next day, ready for another day of school.
          [Days Until Game Over = {timeuntilend}]\n
You arrive at the school gates""")
  dayvalue += 1
  timevalue -= 3
  actionsleft += 3
    
if dayvalue == 6:
  print("""School ends.
It was a short, but sweet adventure.
You reconnected with an old friend, made some new ones and if you are especially unucky, lost one or two.
Let us together see how you did:\n""")
  if maxrelation in range(1 , 25):
    print(f"""Connor Relationship Level = {profiles.Connor.level}
Lana Relationship Level = {profiles.Lana.level}
Stephen Relationship Level = {profiles.Stephen.level}
Sid Relationship Level = {profiles.Sid.level}
Total Relationship Level = {maxrelation} / 100
Rank = 
\nYou Either Did Nothing Or Made Enemys With Everyone!""")
  if maxrelation in range(26 , 50):
    print(f"""Connor Relationship Level = {profiles.Connor.level}
Lana Relationship Level = {profiles.Lana.level}
Stephen Relationship Level = {profiles.Stephen.level}
Sid Relationship Level = {profiles.Sid.level}
Total Relationship Level = {maxrelation} / 100
Rank = 
\nGood Job, But It Could Have Been Better""")
  if maxrelation in range(51 , 75):
    print(f"""Connor Relationship Level = {profiles.Connor.level}
Lana Relationship Level = {profiles.Lana.level}
Stephen Relationship Level = {profiles.Stephen.level}
Sid Relationship Level = {profiles.Sid.level}
Total Relationship Level = {maxrelation} / 100
Rank = 
\nYou Did Really Well! Why Not Try For The Max?""")
  if maxrelation in range(76 , 100):
    print(f"""Connor Relationship Level = {profiles.Connor.level}
Lana Relationship Level = {profiles.Lana.level}
Stephen Relationship Level = {profiles.Stephen.level}
Sid Relationship Level = {profiles.Sid.level}
Total Relationship Level = {maxrelation} / 100
Rank = 
\nHow Did You Even Do That!?""")
  

while True:
  print("\nObjective: Make Friends")
  travel()
  timevalue -= 1
  print(f"You have {actionsleft} actions left.")