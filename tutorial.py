import profiles
import intros

# Tutorial
def tutorial():
  print("\nYour old friend Sid approaches you\n")
  tutorialinput = input("Do you want to talk with him? (Yes) (No):")
  # Decide To Do Tutorial
  if tutorialinput.lower() == "yes":
    print("\nYou go to meet Sid")
    intros.sidintro_1()
    print("""\nYou bid Sid goodbye and enter the school.
You enter the first class you see, art class.""")
    print("""
One of the smaller rooms in the school. 
Inorder to use this small space, 
students have moved the chairs and desks to the far side of the room,
in place of where these school essentials are stools and canvases.
""")
    intros.lanaintro_1()
    print("""\nThe Bell signalling the end of class goes and you swiftly exit.
You get swept up in the crowd of kids.
Next thing you know, you are in a Gym""")
    print("""
A large building connected to the left of the school.
inside there are two basketball hoops on either side of the gym floor.
downstairs is an actual gym.
The students here are mostly doing stretches in preperation for the class.
""")
    intros.connorintro_1()
    print("""\nYou and Connor walk to the main building.
The moment you two enter, you are once again taken by a crowd.
you reach for Connors hand in the sea of students, but he is already gone.
Instead you grab hold of a... textbook!?
Welcome to math class.""")
    print("""
A normal classroom, that is if you look past all the students 
that are outwardly expressing their distane for this class. 
Welcome to Math!
""")
    intros.stephenintro_1()
    print("""\nFor the last time, you are swept up in a crowd as you exit class.
You find yourself at the entrance of the school.
Finally, you get some time to yourself.
Time to officially start your school life!""")
  # Decide Not To Do Tutorial:
  elif tutorialinput.lower() == "no":
    print("\nYou spend the day wandering the halls")
    profiles.Lana.level += 1
    profiles.Connor.level += 7
    profiles.Stephen.level += 3
    profiles.Sid.level += 15
    profiles.Sid.intro += 1