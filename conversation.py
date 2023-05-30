import profiles
import random
import textwrap
Rooms = ("Talk", "Attend Class", "Leave")

#Introductions
def lanaintro():
  print("""\nYou see a girl with a short, black haircut and a tomboyish outfit.
  She is a bit spooked when she sees you.
  A: Are you ok?
  B: Am I getting in the way here?
  C: What are you doing?""")
  lana_introinput = input("Choose: ")
  if lana_introinput.lower() == "a":
    print('“I’m ok. Who are you?”')
    lanaintro()
  elif lana_introinput.lower() == "b":
    print('"No, you are not, I dont think."')
  elif lana_introinput.lower() == "c":
    print('''“Oh, uh, I’m doing art, I guess."\n
    A: What are you painting?
    B: I like it!
    C: Guess it looks ok…''')
    lana_introinput = input("Choose: ")
    if lana_introinput.lower() == "a":
      print('“Just a, uh, landscape.”')
    elif lana_introinput.lower() == "b":
      print('“Oh!”')
      print('''“I didn’t expect anyone would compliment my art…”
      A: What is your name?
      B: You like to paint?
      C: Where'd you learn to paint?''')       
      lana_introinput = input("Choose: ")
      if lana_introinput.lower() == "a":
        print('''“Uhm, it’s…Lana.”
        “Anyways, I have some stuff I need to work on.”
        You leave the room.''')
        profiles.Lana.intro += 1
      
      elif lana_introinput.lower() == "b":
        print('''“Yeah, I do. It’s nice.”
        “Anyways, I have some stuff I need to work on.”
        You leave the room.''')
        profiles.Lana.intro += 1
       
      elif lana_introinput.lower() == "c":
        print('''“Uh, I’d rather not say.”
        “Anyways, I have some stuff I need to work on.”
        You leave the room.''')
        profiles.Lana.intro += 1
        
    elif lana_introinput == "c":
      print('''"Yeah..."
      “Anyways, I have some stuff I need to work on.”
      You leave the room.''')
      profiles.Lana.intro += 1
def connorintro():
  print("""
This is Connor.
Captain of the football team
""")
def stephenintro():
  print("""
This is Stephen.
He is often lost in a book
""")

def sidintro():
  print("""
This is Sid
Your bestfriend from Elementary
""")

  # Converstaion
def lanaconvo():
  lana_pickconvo = random.randint(0, 2)
  while True:
    if lana_pickconvo == 0:
        print("You walk over and talk to Lana.")
        print("A: Talk about art")
        print("B: Talk about school")
        print("C: Talk about home")
        print("D: Talk about video games")
        print("E: Leave")
        lanaconvo_0 = input("Choose: ")
        if lanaconvo_0 == "a":
          print(textwrap.dedent("""You discuss art with Lana. 
You think you could learn some art techniques from her… """))
          profiles.Lana.level += 1
        elif lanaconvo_0 == "b":
          print(textwrap.dedent("""You talk about how school is going. 
Lana seems like she is barely listening."""))
          profiles.Lana.level += 1
        elif lanaconvo_0 == "c":
          print("yeah")
          profiles.Lana.level += 1
        elif lanaconvo_0 == "d":
          if profiles.Lana.level <= 18:
            print("no")
            profiles.Lana.level -= 1
        elif lanaconvo_0 == "e":
          print("You leave.")
          break
    elif lana_pickconvo == 1:
      print("test 1")
      print("- option a")
      print("- option b")
      print("- option c")
      lanaconvo_1 = input("choose: ")
      if lanaconvo_1 == "a":
        print("yeah")
        profiles.Lana.level += 1
      elif lanaconvo_1 == "b":
        print("yeah")
        profiles.Lana.level += 1
      elif lanaconvo_1 == "c":
        print("yeah")
        break
        profiles.Lana.level += 1
    elif lana_pickconvo == 2:
      print("test 2")
      print("- option a")
      print("- option b")
      print("- option c")
      lanaconvo_2 = input("choose: ")
      if lanaconvo == "a":
        print("yeah")
        profiles.Lana.level += 1
      elif lanaconvo_2 == "b":
        print("yeah")
        profiles.Lana.level += 1
      elif lanaconvo_2 == "c":
        print("yeah")
        profiles.Lana.level += 1
def sidconvo():
    sid_pickconvo = random.randint(0, 2)
    if sid_pickconvo == 0:
      print("test 0")
      print("- option a")
      print("- option b")
      print("- option c")
      print("- option d")
      sidconvo_0 = input("choose: ")
      if sidconvo_0 == "a":
        print("yeah")
        profiles.Sid.level += 1
      elif sidconvo_0 == "b":
        print("yeah")
        profiles.Sid.level += 1
      elif sidconvo_0 == "c":
        print("yeah")
        profiles.Sid.level += 1
      elif sidconvo_0 == "d":
        if profiles.Sid.level <= 18:
          print("no")
    elif sid_pickconvo == 1:
      print("test 1")
      print("- option a")
      print("- option b")
      print("- option c")
      sidconvo_1 = input("choose: ")
      if sidconvo_1 == "a":
        print("yeah")
        profiles.Sid.level += 1
      elif sidconvo_1 == "b":
        print("yeah")
        profiles.Sid.level += 1
      elif sidconvo_1 == "c":
        print("yeah")
        profiles.Sid.level += 1
    elif sid_pickconvo == 2:
      print("test 2")
      print("- option a")
      print("- option b")
      print("- option c")
      sidconvo_2 = input("choose: ")
      if sidconvo_2 == "a":
        print("yeah")
        profiles.Sid.level += 1
      elif sidconvo_2 == "b":
        print("yeah")
        profiles.Sid.level += 1
      elif sidconvo_2 == "c":
        print("yeah")
        profiles.Sid.level += 1
def connorconvo():
  fhghg
def stephenconvo():
  jgjgjhh
  
  # Game Over (Below 0)