import textwrap
import profiles

def lanaintro_end():
  print(textwrap.dedent("""“Anyways, I have some stuff I need to work on.”
You leave the room."""))
  profiles.Lana.intro += 1

def lanaintro_3():
  print(textwrap.dedent("""A: What is your name?
B: You like to paint?
C: Where'd you learn to paint?"""))       
  lana_introinput = input("Choose: ")
  if lana_introinput.lower() == "a":
        print('''\n“Uhm, it’s…Lana.”''')
        lanaintro_end()
  elif lana_introinput.lower() == "b":
        print('''\n“Yeah, I do. It’s nice.”''')
        lanaintro_end()
  elif lana_introinput.lower() == "c":
        print('''\n“Uh, I’d rather not say.”''')
        lanaintro_end()
    
def lanaintro_2():
  print(textwrap.dedent("""A: What are you painting?
B: I like it!
C: Guess it looks ok…"""))
  lana_introinput = input("Choose: ")
  if lana_introinput.lower() == "a":
      print('\n“Just a, uh, landscape.”')
      lanaintro_3()
  elif lana_introinput.lower() == "b":
      print('''\n“Oh! I didn’t expect anyone would compliment my art…”''')
      lanaintro_3()
  elif lana_introinput == "c":
      print("Yeah...")
      lanaintro_3()

def lanaintro_1():
  print("""\nYou see a girl with a short, black haircut and a tomboyish outfit.
  She is a bit spooked when she sees you.
  A: Are you ok?
  B: Am I getting in the way here?
  C: What are you doing?""")
  lana_introinput = input("Choose: ")
  if lana_introinput.lower() == "a":
    print('\n“I’m ok. Who are you?”')
    lanaintro_2()
  elif lana_introinput.lower() == "b":
    print('\n"No, you are not, I dont think."')
    lanaintro_2()
  elif lana_introinput.lower() == "c":
    print('''\n“Oh, uh, I’m doing art, I guess."\n''')
    lanaintro_2()