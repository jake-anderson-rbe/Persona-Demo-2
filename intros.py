import profiles










# Yo, Good Morning, Quick message from the rat man
# If you use "" in a print, use it like this print('''"Hello"''')
# Not print(""" "Hello" """)








def lanaintro_end():
  print('''“Anyways, I have some stuff I need to work on.”
You leave the room.''')
  profiles.Lana.intro += 1

def lanaintro_3():
  print("""A: What is your name?
B: You like to paint?
C: Where'd you learn to paint?""")
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
  print("""A: What are you painting?
B: I like it!
C: Guess it looks ok…""")
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

def connorintro_end():
  print("""“Well, I got a game to practice for.
Guess I’ll see you around.”""")
  print("You leave the gym.")
  profiles.Connor.intro += 1

def connorintro_2():
  print("""A: You on the basketball team?
B: Is there anything I can check out here?
C: Can I play against you?""")
  connor_introinput = input("Choose: ")
  if connor_introinput.lower() == "a":
        print("""“Basketball AND football team.
Captain for both.” """)
        connorintro_end()
  elif connor_introinput.lower() == "b":
         print('''“You can join the guys doing yoga there, 
but right now, there’s not much.” ''')
         connorintro_end()
  elif connor_introinput.lower() == "c":
         print('''“In your dreams, buddy.”''')
         connorintro_end()

def connorintro_1():
  print("""You enter the gym, 
and see a tall boy, dribbling a basketball.
He spots you looking at him.
“What are you doing?""")
  print("""A: Oh, uh, I’m just wandering around.
B: Just checking out what’s here in the gym.
C: What are you doing?""")
  connor_introinput = input("Choose: ")
  if connor_introinput.lower() == "a":
        print('''“Huh, I see. Cool.”''')
        connorintro_2()
  elif connor_introinput.lower() == "b":
         print('''“Sports, obviously.”''')
         connorintro_2()
  elif connor_introinput.lower() == "c":
         print('''“I’m practicing. 
We have a big game coming up soon.
I’m making sure I won’t lose.”''')
         connorintro_2()

def sidintro_end():
  print('''“Well, would you look at the time.
I gotta run to class! 
See you later, dude!”''')
  print("He rushes off.")
  profiles.Sid.intro += 1

def sidintro_2():
  print('''“So, you excited? 
Heard this school is great when it comes to the ladies.”
A: Sure.
B: Not really.''')
  sid_introinput = input("Choose: ")
  if sid_introinput.lower() == "a":
        print('''“I’d be excited too; 
there’s a lot of cool stuff here.” ''')
        sidintro_end()
  elif sid_introinput.lower() == "b":
        print('''“Oh c’mon! 
You really gotta get your head out of the gutter. 
You don’t wanna be a buzzkill!” ''')
        sidintro_end()

def sidintro_1():
  print('''As you enter the school,
you see a familiar face at the entrance.
It’s Sid, one of your old school friends. 
“Well, look who it is! How’s it been going?”''')
  print("""A: Good!
B: I'm so-so.
C: You’ve changed.""")
  sid_introinput = input("Choose: ")
  if sid_introinput.lower() == "a":
        print('''“Ain’t that just grand!
Wondered how you were, since we stopped talking.”''')
        sidintro_2()
  elif sid_introinput.lower() == "b":
         print('''“Oh, really? 
You need to chin up, at least for the ladies.”''')
         sidintro_2()
  elif sid_introinput.lower() == "c":
         print('''“Huh? What do you mean by ‘changed’?
Y'know what, it's fine.”''')
         sidintro_2()

def stephenintro_end():
  print('''“I don’t mean to be rude, but could you go? 
I need to finish all of this.”''')
  print("You leave the room.")
  profiles.Stephen.intro += 1

def stephenintro_2():
  print("""A: I like math too.
B: You studying?
C: You sure you don’t need any help?""")
  connor_introinput = input("Choose: ")
  if connor_introinput.lower() == "a":
        print('''“Oh, you do? That’s neat!”''')
        stephenintro_end()
  elif connor_introinput.lower() == "b":
         print('''“No, I’m just doing this for fun.”''')
         stephenintro_end()
  elif connor_introinput.lower() == "c":
         print('''“Dude, it’s ok, I’m fine.”''')
         stephenintro_end()

def stephenintro_1():
  print("""A: What are you doing?
B: That looks hard!
C: Uh, do you need any help?""")
  connor_introinput = input("Choose: ")
  if connor_introinput.lower() == "a":
        print('''“Math, pythagorean theorem specifically.”''')
        stephenintro_2()
  elif connor_introinput.lower() == "b":
         print('''“I mean, it really isn’t. 
When you know what you’re doing.”''')
         stephenintro_2()
  elif connor_introinput.lower() == "c":
         print('''“Nope.”''')
         stephenintro_2()