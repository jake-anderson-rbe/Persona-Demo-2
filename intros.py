import profiles


def lanaintro_end():
    #"""Code defining end of Lana's intro"""
    print('''“Anyways, I have some stuff I need to work on.”
You leave the room.''')
    profiles.Lana.intro += 1 # Lana intro is now complete

def lanaintro_3():
    """Code defining third section of Lana's intro"""
    print("""A: What is your name?
B: You like to paint?
C: Where'd you learn to paint?""")
    lana_introinput = input("Choose: ")
    if lana_introinput.lower() == "a":
        print('''\n“Uhm, it’s…Lana.”\n''')
        lanaintro_end()
    elif lana_introinput.lower() == "b":
        print('''\n“Yeah, I do. It’s nice.”\n''')
        lanaintro_end()
    elif lana_introinput.lower() == "c":
        print('''\n“Uh, I’d rather not say.”\n''')
        lanaintro_end()
    else:
        print("Invalid input!\n")
        lanaintro_3()
    
def lanaintro_2():
    #"""Code defining second section of Lana's intro"""
    print("""A: What are you painting?
B: I like it!
C: Guess it looks ok…""")
    lana_introinput = input("Choose: ")
    if lana_introinput.lower() == "a":
        print('\n“Just a, uh, landscape.”\n')
        lanaintro_3()
    elif lana_introinput.lower() == "b":
        print('''\n“Oh! I didn’t expect anyone would compliment my art…”\n''')
        lanaintro_3()
    elif lana_introinput.lower() == "c":
        print("\nYeah...\n")
        lanaintro_3()
    else:
        print("Invalid input!\n")
        lanaintro_2()

def lanaintro_1():
    #"""Code defining first section of Lana's intro"""
    print("""\nYou see a girl with a short, black haircut and a tomboyish outfit.
She is a bit spooked when she sees you.\n
A: Are you ok?
B: Am I getting in the way here?
C: What are you doing?""")
    lana_introinput = input("Choose: ")
    if lana_introinput.lower() == "a":
          print('\n“I’m ok. Who are you?”\n')
          lanaintro_2()
    elif lana_introinput.lower() == "b":
        print('\n"No, you are not, I dont think."\n')
        lanaintro_2()
    elif lana_introinput.lower() == "c":
        print('''\n“Oh, uh, I’m doing art, I guess."\n''')
        lanaintro_2()
    else:
        print("Invalid input!\n")
        lanaintro_1()

  
def connorintro_end():
    #"""Code defining end of Connor's intro"""
    print("""\n“Well, I got a game to practice for.
Guess I’ll see you around.”""")
    print("You leave the gym.")
    profiles.Connor.intro += 1 # Connor intro is now complete

def connorintro_2():
    # Code defining second section of Connor's intro
    print("""A: You on the basketball team?
B: Is there anything I can check out here?
C: Can I play against you?""")
    connor_introinput = input("Choose: ")
    if connor_introinput.lower() == "a":
        print("""\n“Basketball AND football team.
Captain for both.” """)
        connorintro_end()
    elif connor_introinput.lower() == "b":
        print('''\n“You can join the guys doing yoga there, 
but right now, there’s not much.” ''')
        connorintro_end()
    elif connor_introinput.lower() == "c":
        print('''\n“In your dreams, buddy.”''')
        connorintro_end()
    else:
        print("Invalid input!\n")
        connorintro_2()

def connorintro_1():
    """Code defining first section of Connor's intro"""
    print("""\nYou enter the gym, 
and see a tall boy, dribbling a basketball.
He spots you looking at him.
“What are you doing?\n""")
    print("""A: Oh, uh, I’m just wandering around.
B: Just checking out what’s here in the gym.
C: What are you doing?""")
    connor_introinput = input("Choose: ")
    if connor_introinput.lower() == "a":
        print('''\n“Huh, I see. Cool.”\n''')
        connorintro_2()
    elif connor_introinput.lower() == "b":
         print('''\n“Sports, obviously.”\n''')
         connorintro_2()
    elif connor_introinput.lower() == "c":
         print('''\n“I’m practicing. 
We have a big game coming up soon.
I’m making sure I won’t lose.”\n''')
         connorintro_2()
    else:
        print("Invalid input!\n")
        connorintro_1()

      
def sidintro_end():
    #"""Code defining end of Sid's intro"""
    print('''\n“Well, would you look at the time.
I gotta run to class! 
See you later, dude!”''')
    print("He rushes off.")
    profiles.Sid.intro += 1

def sidintro_2():
    #"""Code defining second section of Sid's intro"""
    print('''“So, you excited? 
Heard this school is great when it comes to the ladies.”\n
A: Sure.
B: Not really.''')
    sid_introinput = input("Choose: ")
    if sid_introinput.lower() == "a":
        print('''\n“I’d be excited too; 
there’s a lot of cool stuff here.”''')
        sidintro_end()
    elif sid_introinput.lower() == "b":
        print('''\n“Oh c’mon! 
You really gotta get your head out of the gutter. 
You don’t wanna be a buzzkill!”''')
        sidintro_end()
    else:
        print("Invalid input!\n")
        sidintro_2()

def sidintro_1():
    #"""Code defining first section of Sid's intro"""
    print('''\nAs you enter the school,
you see a familiar face at the entrance.
It’s Sid, one of your old school friends. 
“Well, look who it is! How’s it been going?”\n''')
    print("""A: Good!
B: I'm so-so.
C: You’ve changed.""")
    sid_introinput = input("Choose: ")
    if sid_introinput.lower() == "a":
        print('''\n“Ain’t that just grand!
Wondered how you were, since we stopped talking.”\n''')
        sidintro_2()
    elif sid_introinput.lower() == "b":
         print('''\n“Oh, really? 
You need to chin up, at least for the ladies.”\n''')
         sidintro_2()
    elif sid_introinput.lower() == "c":
         print('''\n“Huh? What do you mean by ‘changed’?
Y'know what, it's fine.”\n''')
         sidintro_2()
    else:
        print("Invalid input!\n")
        sidintro_1()


def stephenintro_end():
    #"""Code defining end of Stephen's intro"""
    print('''\n“I don’t mean to be rude, but could you go? 
I need to finish all of this.”''')
    print("You leave the room.")
    profiles.Stephen.intro += 1

def stephenintro_2():
    #"""Code defining second section of Stephen's intro"""
    print("""A: I like math too.
B: You studying?
C: You sure you don’t need any help?""")
    stephen_introinput = input("Choose: ")
    if stephen_introinput.lower() == "a":
        print('''\n“Oh, you do? That’s neat!”''')
        stephenintro_end()
    elif stephen_introinput.lower() == "b":
         print('''\n“No, I’m just doing this for fun.”''')
         stephenintro_end()
    elif stephen_introinput.lower() == "c":
         print('''\n“Dude, it’s ok, I’m fine.”''')
         stephenintro_end()
    else:
         print("Invalid input!\n")
         stephenintro_2()

def stephenintro_1():
    #"""Code defining first section of Stephen's intro"""
    print("""\nYou enter the science room, and see a kid 
sitting at a desk.
He’s doing some experiments, and they look complex.\n""")
    print("""A: What are you doing?
B: That looks hard!
C: Uh, do you need any help?""")
    stephen_introinput = input("Choose: ")
    if stephen_introinput.lower() == "a":
        print('''\n“Math, pythagorean theorem specifically.”\n''')
        stephenintro_2()
    elif stephen_introinput.lower() == "b":
         print('''\n“I mean, it really isn’t. 
When you know what you’re doing.”\n''')
         stephenintro_2()
    elif stephen_introinput.lower() == "c":
         print('''\n“Nope.”\n''')
         stephenintro_2()
    else:
         print("Invalid input!\n")
         stephenintro_1()