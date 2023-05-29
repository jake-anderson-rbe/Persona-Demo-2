import profiles
import random
Rooms = ("Talk", "Attend Class", "Leave")

#Introductions
def lanaintro():
  print("You see a girl with a short, black haircut and a tomboyish outfit. ")
  print("She is a bit spooked when she sees you.")
  print("A: Are you ok?")
  print("B: Am I getting in the way here?")
  print("C: What are you doing?")
  print("D: Leave")
  while True:
    lana_introinput = input("Choose: ")
    if lana_introinput.lower() == "a":
        print("“I’m ok. Who are you?”")
    elif lana_introinput.lower() == "b":
        print("“No, you aren't, I don’t think.”")
    elif lana_introinput.lower() == "c":
        print("“Oh, uh, I’m doing art, I guess.\n”")
        print("A: What are you painting?")
        print("B: I like it!")
        print("C: Guess it looks ok…")
        print("D: Leave\n")
        while True:
          lana_introinput = input("Choose: ")
          if lana_introinput.lower() == "a":
            print("“Just a, uh, landscape.”")
          if lana_introinput.lower() == "b":
            print("“Oh!”")
            print("""“I didn’t expect anyone would compliment my art…”
            A: What is your name?
            B: You like to paint?
            C: Where'd you learn to paint?""")
            while True:
              lana_introinput = input("Choose: ")
              if lana_introinput.lower() == "a":
                print("“Uhm, it’s…Lana.”")
              elif lana_introinput.lower() == "b":
                print("“Yeah, I do. It’s nice.”")
              elif lana_introinput.lower() == "c":
                print("“Uh, I’d rather not say.”")
          elif lana_introinput == "c":
                print("Yeah...")
                profiles.Lana.intro += 1
    elif lana_introinput == "d":
      break
    print("“Anyways, I have some stuff I need to work on.”")
    print("You leave the room.")
    profiles.Lana.intro += 1
    break
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
        print("- Talk about art")
        print("- Talk about school")
        print("- Talk about home")
        print("- Talk about home")
        lanaconvo_0 = input("choose: ")
        if lanaconvo_0 == "a":
          print("yeah")
          profiles.Lana.level += 1
        elif lanaconvo_0 == "b":
          print("yeah")
          profiles.Lana.level += 1
        elif lanaconvo_0 == "c":
          print("yeah")
          profiles.Lana.level += 1
        elif lanaconvo_0 == "d":
          if profiles.Lana.level <= 18:
            print("no")
            profiles.Lana.level -= 1
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