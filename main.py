import intros
import sys
import map
import conversation
import profiles
import classes
import random
import tutorial

timeuntilend = 6
actionsleft = 5
maxrelation = 25




# Each Class
  # Art Class
def art():
  print(f"\n{map.Art.discription}")
  if profiles.Lana.intro == 0:
    print("You spot someone painting in the corner.")
  elif profiles.Lana.intro == 1:
    print(f"You see {map.Art.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input.lower() == "talk":
    if profiles.Lana.intro == 0:
      intros.lanaintro_1()
    elif profiles.Lana.intro == 1:
      conversation.lanaconvo()
    elif profiles.Lana.level >= 25:
      print("You Already Reached Max Relationship Level With This Person")
      menu()
  elif decide_input == "attend class":
    classes.attendart()
  elif decide_input.lower() == "leave":
    menu()    
  # Math Class
def math():
  print(f"{map.Math.discription}")
  print(f"You see {map.Math.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input.lower() == "talk":
    if profiles.Connor.intro == 0:
      print("""They seem wary of you. 
Maybe talk to them when they are in a place more familiar to them.""")
    elif profiles.Connor.intro == 1:
      classes.connorconvo()
    elif profiles.Connor.level >= 25:
      print("You Already Reached Max Relationship Level With This Person")
      menu()
  elif decide_input.lower() == "attend class":
    classes.attendmath()
  elif decide_input.lower() == "leave":
    menu()   
  # Social Class
def social():
  print(f"{map.Social.discription}")
  print(f"You see {map.Social.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input.lower() == "talk":
    if profiles.Lana.intro == 0:
      print("""They seem wary of you. 
Maybe talk to them when they are in a place more familiar to them.""")
    elif profiles.Lana.intro >= 1:
      conversation.lanaconvo()
    if profiles.Lana.level == 25:
        print("You Already Reached Max Relationship Level With This Person")
        menu()
  elif decide_input.lower() == "attend class":
    classes.attendsocial()
  elif decide_input.lower() == "leave":
    menu()
  # Science Class
def science():
  print(f"{map.Science.discription}")
  print(f"You see {map.Science.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input.lower() == "talk":
    if profiles.Stephen.intro == 0:
       print("""They seem wary of you. 
Maybe talk to them when they are in a place more familiar to them.""")
    elif profiles.Stephen.intro == 1:
      classes.stephenconvo()
    elif profiles.Stephen.level >= 25:
      print("You Already Reached Max Relationship Level With This Person")
      menu()
  elif decide_input.lower() == "attend xlass":
    classes.attendscience()
  elif decide_input.lower() == "leave":
    menu()
  # Gym Class
def gym():
  print(f"{map.Gym.discription}")
  if profiles.Connor.intro == 0:
    print("You see someone interesting in the gym.")
  elif profiles.Connor.intro == 1:
    print(f"You see {map.Gym.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input.lower() == "talk":
    if profiles.Connor.intro == 0:
      conversation.connorintro()
    elif profiles.Connor.intro == 1:
      conversation.connorconvo()
    elif profiles.Connor.level >= 25:
      print("You Already Reached Max Relationship Level With This Person")
      menu()
  elif decide_input.lower() == "attend class":
    classes.attendgym()
  elif decide_input.lower() == "leave":
    menu()   
  # pool Class
def pool():
  print(f"{map.Pool.discription}")
  print(f"You see {map.Pool.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input.lower() == "talk":
    if profiles.Sid.level == 1:
      conversation.sidconvo()
    elif profiles.Sid.level >= 25:
      print("You Already Reached Max Relationship Level With This Person")
      menu()
  elif decide_input.lower() == "attend class":
    classes.attendpool()
  elif decide_input.lower() == "leave":
    menu()
  # ELA Class
def ela():
  print(f"{map.ELA.discription}")
  print(f"You see {map.ELA.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input.lower() == "talk":
    characterchosen = input("Who do you want to talk to? :")
    if characterchosen.lower() == "sid":
      if profiles.Sid.level == 1:
        conversation.sidconvo()
      elif profiles.Sid.level >= 25:
        print("You Already Reached Max Relationship Level With This Person")
        menu()
    if characterchosen.lower() == "lana":
      if profiles.Lana.intro == 0:
         print("""They seem wary of you. 
Maybe talk to them when they are in a place more familiar to them.""")
      elif profiles.Lana.intro >= 1:
        conversation.lanaconvo()
      elif profiles.Lana.level >= 25:
        print("You Already Reached Max Relationship Level With This Person")
        menu()
  elif decide_input.lower() == "attend class":
    classes.attendela()
  elif decide_input.lower() == "leave":
    menu()
  # Club Building Class
def club():
  print(f"{map.Club.discription}")
  print(f"You see {map.Club.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input.lower() == "talk":
    characterchosen = input("Who do you want to talk to? :")
    if characterchosen.lower() == "sid":
      if profiles.Sid.intro == 1:
        conversation.sidconvo()
      elif profiles.Sid.level >= 25:
        print("You Already Reached Max Relationship Level With This Person")
        menu()
    if characterchosen.lower() == "lana":
      if profiles.Lana.intro == 0:
         print("""They seem wary of you. 
Maybe talk to them when they are in a place more familiar to them.""")
      elif profiles.Lana.intro == 1:
        conversation.lanaconvo()
      elif profiles.Lana.level >= 25:
        print("You Already Reached Max Relationship Level With This Person")
        menu()
  elif decide_input.lower() == "attend class":
    classes.attendclub()
  elif decide_input.lower() == "leave":
    menu()
  # Track Class
def track():
  print(f"{map.Track.discription}")
  print(f"You see {map.Track.character}")
  for decide in conversation.Rooms:
    print(f"{decide}")
  decide_input = input("What do you do?: ")
  if decide_input.lower() == "talk":
    characterchosen = input("Who do you want to talk to? :")
    if characterchosen.lower() == "stephen":
      if profiles.Stephen.intro == 0:
         print("""They seem wary of you. 
Maybe talk to them when they are in a place more familiar to them.""")
      elif profiles.Stephen.intro == 1:
        conversation.stephenconvo()
      elif profiles.Stephen.level >= 25:
        print("You Already Reached Max Relationship Level With This Person")
        menu()
    if characterchosen.lower() == "connor":
      if profiles.Connor.intro == 0:
         print("""They seem wary of you. 
Maybe talk to them when they are in a place more familiar to them.""")
      elif profiles.Connor.intro >= 1:
        conversation.connorconvo()
      elif profiles.Connor.level >= 25:
        print("You Already Reached Max Relationship Level With This Person")
        menu()
  elif decide_input.lower() == "attend class":
    classes.attendtrack()
  elif decide_input.lower() == "leave":
    menu()


# Tutorial Main
print("Welcome to HighSchool")
print("You just transfered here as a 2nd year and know nobody here.")
print("Except your best friend from elementary, Sid.")
print("""But one friend isnt enough to get you through this battleground. 
so why not go out and make some more""")
print("\nObjective: Meet Fellow Students ")

# Starting and Ending Tutorial
tutorial.tutorial()
actionsleft -= 5

# Day Ends, Activities and Ending
  # No More Actions + Day Reset
if actionsleft == 0:
  timeuntilend -= 1
  print(f"""\nAfter a busy day at school, 
it seems time to head home.\n
You wake up the next day, ready for another day of school.
[Days Until Game Over = {timeuntilend}]\n
You arrive at the school gates""")
  actionsleft += 5 
  # Time Limit Ends + End Of Game
if timeuntilend == 0:
  print("""School ends.
It was a short, but sweet adventure.
You reconnected with an old friend, made some new ones and if you are especially unucky, lost one or two.
Let us together see how you did:\n""")
  if maxrelation in range(0 , 26):
    print(f"""Connor Relationship Level = {profiles.Connor.level}
Lana Relationship Level = {profiles.Lana.level}
Stephen Relationship Level = {profiles.Stephen.level}
Sid Relationship Level = {profiles.Sid.level}
Total Relationship Level = {maxrelation} / 100
\nRank = F
\nYou Either Did Nothing Or Made Enemys With Everyone!""")
    sys.exit()
  if maxrelation in range(25 , 51):
    print(f"""Connor Relationship Level = {profiles.Connor.level}
Lana Relationship Level = {profiles.Lana.level}
Stephen Relationship Level = {profiles.Stephen.level}
Sid Relationship Level = {profiles.Sid.level}
Total Relationship Level = {maxrelation} / 100
\nRank = C
\nGood Job, But It Could Have Been Better""")
    sys.exit()
  if maxrelation in range(50 , 76):
    print(f"""Connor Relationship Level = {profiles.Connor.level}
Lana Relationship Level = {profiles.Lana.level}
Stephen Relationship Level = {profiles.Stephen.level}
Sid Relationship Level = {profiles.Sid.level}
Total Relationship Level = {maxrelation} / 100
\nRank = B
\nYou Did Really Well! Why Not Try For The Max?""")
    sys.exit()
  if maxrelation in range(75 , 101):
    print(f"""Connor Relationship Level = {profiles.Connor.level}
Lana Relationship Level = {profiles.Lana.level}
Stephen Relationship Level = {profiles.Stephen.level}
Sid Relationship Level = {profiles.Sid.level}
Total Relationship Level = {maxrelation} / 100
\nRank = *A*
\nHow Did You Even Do That!?""")
    sys.exit()




# System for getting around
def travel():
  print("\nyou can go to:")
  for school_location in map.school_locations:
    print(school_location)
  movement_input = input("where do you go? ")
  # First Floor Options
  if movement_input.lower() == "1st floor":
    print("\nyou can go to:")
    for first_location in map.first_locations:
      print(first_location)
    movement_input = input("where do you go? ")
    if movement_input.lower() == "math":
      math()
    if movement_input.lower() == "social":
      social()
    if movement_input.lower() == "art":
      art()
  # Second Floor Options
  elif movement_input.lower() == "2nd floor":
    print("\nyou can go to:")
    for second_location in map.second_locations:
      print(second_location)
    movement_input = input("where do you go? ")
    if movement_input.lower() == "ela":
      ela()
    if movement_input.lower() == "science":
      science()
  # Yard Options
  elif movement_input.lower() == "yard":
    print("\nyou can go to:")
    for yard_location in map.yard_locations:
      print(yard_location)
    movement_input = input("where do you go? ")
    if movement_input.lower() == "gym":
      gym()
    if movement_input.lower() == "club building":
      club()
    if movement_input.lower() == "pool":
      pool()
    if movement_input.lower() == "track field":
      track()
  elif movement_input.lower() == "menu":
    menu()

  # Error Message
  else:
    print("\nYou end up back at the entrance.")
    travel()


# Main
  # Menu
def menu():
  print("""\nWhat would you like to do?
- Move
- Check Relationships
- Hints
- Quit""")
  menu_input = input("Choose: ")
  if menu_input.lower() == "move":
    travel()
  elif menu_input.lower() == "check relationships":
      print(f"""{profiles.Lana.name}, Level: {profiles.Lana.level}
{profiles.Connor.name}, Level:{profiles.Connor.level}
{profiles.Sid.name}, Level: {profiles.Sid.level}
{profiles.Stephen.name}, Level: {profiles.Stephen.level}""")
      menu()
  elif menu_input.lower() == "hints":
    hint_selection = random.randint(0, 4)
    if hint_selection == 0:
      print("""If a character’s relationship level goes down in a conversation,
that means you’ll have to unlock it later.""")
      menu()
    elif hint_selection == 1:
      print("""If you get a message when you reach a certain relationship level
with a character saying you’ve grown closer,
that means a dialogue option has unlocked.""")
      menu()
    elif hint_selection == 2:
      print("""Conversations are great, but you can also raise relationship levels
by attending classes.""")
      menu()
    elif hint_selection == 3:
      print("""If a character is wary of you, 
you may have to introduce yourself to them in a place
where they are more comfortable.""")
      menu()
    elif hint_selection == 4:
      print("""Unlocked dialogue options, 
while giving you more relationship levels, 
can only be used once.""")
      menu()
  elif menu_input.lower() == "quit":
      print("Goodbye!")
      sys.exit()
  elif menu_input == "lana test":
      print("lana intro complete")
      profiles.Lana.intro += 1
      menu()
  else:
    print("Incorrect input!")
    menu()

  # Relation Growth Notif
if profiles.Lana.level == 10:
  print("You have become a lot closer to Lana.")
elif profiles.Lana.level == 15:
  print("You now feel very close with Lana.")
elif profiles.Connor.level == 10:
  print("You have become a lot closer to Connor.")
elif profiles.Connor.level == 15:
  print("You now feel very close with Connor.")
elif profiles.Stephen.level == 10:
  print("You now feel a lot closer with Stephen.")

 # Loop Main
while True:
  print("\nObjective: Make Friends")
  menu()
  print(f"\nYou have {actionsleft} actions left.")
  if actionsleft == 0:
    print("""The day is over, and you return home.
***
You return the next day.""")
    actionsleft += 5
    timeuntilend -= 1
    print(f"[Days Left: {timeuntilend}]")
  if timeuntilend == 0:
    print("""School ends.
It was a short, but sweet adventure.
You reconnected with an old friend, made some new ones and if you are especially unucky, lost one or two.
Let us together see how you did:\n""")
    if maxrelation in range(0 , 26):
      print(f"""Connor Relationship Level = {profiles.Connor.level}
Lana Relationship Level = {profiles.Lana.level}
Stephen Relationship Level = {profiles.Stephen.level}
Sid Relationship Level = {profiles.Sid.level}
Total Relationship Level = {maxrelation} / 100
\nRank = F
\nYou Either Did Nothing Or Made Enemys With Everyone!""")
      sys.exit()
    if maxrelation in range(25 , 51):
      print(f"""Connor Relationship Level = {profiles.Connor.level}
Lana Relationship Level = {profiles.Lana.level}
Stephen Relationship Level = {profiles.Stephen.level}
Sid Relationship Level = {profiles.Sid.level}
Total Relationship Level = {maxrelation} / 100
\nRank = C
\nGood Job, But It Could Have Been Better""")
      sys.exit()
    if maxrelation in range(50 , 76):
      print(f"""Connor Relationship Level = {profiles.Connor.level}
Lana Relationship Level = {profiles.Lana.level}
Stephen Relationship Level = {profiles.Stephen.level}
Sid Relationship Level = {profiles.Sid.level}
Total Relationship Level = {maxrelation} / 100
\nRank = B
\nYou Did Really Well! Why Not Try For The Max?""")
      sys.exit()
    if maxrelation in range(75 , 101):
      print(f"""Connor Relationship Level = {profiles.Connor.level}
Lana Relationship Level = {profiles.Lana.level}
Stephen Relationship Level = {profiles.Stephen.level}
Sid Relationship Level = {profiles.Sid.level}
Total Relationship Level = {maxrelation} / 100
\nRank = *A*
\nHow Did You Even Do That!?""")
      sys.exit()