import profiles
import random
import textwrap
Rooms = ("Talk", "Attend Class", "Leave")

#Introductions
  # Lana Intro
def lanaintro():
  print("""\nYou see a girl with a short, black haircut and a tomboyish outfit.
  She is a bit spooked when she sees you.
  A: Are you ok?
  B: Am I getting in the way here?
  C: What are you doing?""")
  lana_introinput = input("Choose: ")
  if lana_introinput.lower() == "a":
    print('\n“I’m ok. Who are you?”')
    lanaintro()
  elif lana_introinput.lower() == "b":
    print('\n"No, you are not, I dont think."')
  elif lana_introinput.lower() == "c":
    print('''\n“Oh, uh, I’m doing art, I guess."\n
    A: What are you painting?
    B: I like it!
    C: Guess it looks ok…''')
    lana_introinput = input("Choose: ")
    if lana_introinput.lower() == "a":
      print('\n“Just a, uh, landscape.”')
    elif lana_introinput.lower() == "b":
      print('''\n“Oh! I didn’t expect anyone would compliment my art…”
      A: What is your name?
      B: You like to paint?
      C: Where'd you learn to paint?''')       
      lana_introinput = input("Choose: ")
      if lana_introinput.lower() == "a":
        print('''\n“Uhm, it’s…Lana.”
        “Anyways, I have some stuff I need to work on.”
        You leave the room.''')
        profiles.Lana.intro += 1
      
      elif lana_introinput.lower() == "b":
        print('''\n“Yeah, I do. It’s nice.”
        “Anyways, I have some stuff I need to work on.”
        You leave the room.''')
        profiles.Lana.intro += 1
       
      elif lana_introinput.lower() == "c":
        print('''\n“Uh, I’d rather not say.”
        “Anyways, I have some stuff I need to work on.”
        You leave the room.''')
        profiles.Lana.intro += 1
        
    elif lana_introinput == "c":
      print('''
      "Yeah..."
      “Anyways, I have some stuff I need to work on.”
      You leave the room.''')
      profiles.Lana.intro += 1
  # Connor Intro
def connorintro():
  print("""
This is Connor.
Captain of the football team
""")
  # Stephen Intro
def stephenintro():
  print("""
This is Stephen.
He is often lost in a book
""")
  # Sid Intro
def sidintro():
  print("""
This is Sid
Your bestfriend from Elementary
""")




# Converstaion
# Lana Convo
def lanaconvo():
  lana_pickconvo = random.randint(0, 2)
  print("You walk over and talk to Lana.")
  while True:
    if lana_pickconvo == 0:
        print(textwrap.dedent("""A: Talk about art
B: Talk about school
C: Talk about home
D: Talk about video games
E: Leave"""))
        lanaconvo_0 = input("Choose: ")
        if lanaconvo_0 == "a":
            print("""You discuss art with Lana. 
You think you could learn some art techniques from her… 
[Relationship Increased by 1""")
            profiles.Lana.level += 1
        elif lanaconvo_0 == "b":
            print("""You talk about how school is going. 
Lana seems like she is barely listening.
[No Relationship Gain""")
        elif lanaconvo_0 == "c":
          if profiles.Lana.level <= 10:
            print("""You try to talk about your home life, 
but Lana shoots you a glare.
You may need to grow closer before talking about this.
[Relationship Decreased by 1]""")
            profiles.Lana.level -= 1
          elif profiles.Lana.level >= 10:
            profiles.Lana.level += 4
            print("""You ask Lana about her home life. 
She sighs.
“I dunno. My parents aren’t the best.
They all seem so focused on work and whatever new fad they’ve found.
Usually, it’s like I’m a ghost to them. Like I don’t exist.”
She sighs again, before looking up at you.
“Oh, uh, I didn’t mean to get all that depressing.”
She laughs to herself, and looks at you.
“Either way, thanks for listening. I needed to get that off my chest.”
[Relationship Increased by 4]""")
            #lana_dialoguecomplete1 += 1
          #elif lana_dialoguecomplete1 == 1:
            #print("Lana already felt comfortable to talk to you about that.")
        elif lanaconvo_0 == "d":
            print("""You talk about a new game that came out. 
Lana seems interested.
[Relationship Increased by 1]""")
            profiles.Lana.level += 1
        elif lanaconvo_0 == "e":
            print("You leave.")
            break
    elif lana_pickconvo == 1:
      print(textwrap.dedent("""A: Talk about homework
B: Talk about local events
C: Talk about gossip
D: Talk about family
E: Leave"""))
      lanaconvo_1 = input("choose: ")
      if lanaconvo_1 == "a":
          print("""You talk about some homework you have been assigned.
She seems sympathetic but uninterested.
[No Relationship Gain]""")
      elif lanaconvo_1 == "b":
          print("""You talk about an event that’s happening soon. 
Lana seems somewhat curious.
[Relationship Increased by 1]""")
          profiles.Lana.level += 1
      elif lanaconvo_1 == "c":
          print("""You ask Lana if she’s heard any gossip around school.
She does mention that she heard rumors about a couple that split up recently.
[No Relationship Gain]""")
      elif lanaconvo_1 == "d":
        if profiles.Lana.level <= 15:
          print("""You try to talk about your family,
but Lana seems a bit down when you mention it.
You may need to grow closer before talking about this.
[Relationship Decreased by 1]""")
          profiles.Lana.level -= 1
        elif profiles.Lana.level >= 15:
          print("""You talk about your family, 
and Lana looks at you, then speaks:
“I wish my family was like that. My dad is usually too drunk to stand. 
He yells a lot, too…”
She looks down at the floor.
“Hopefully, I can move out one day. Do my own thing. That’d be nice.”
She looks at you again.
“Maybe we can still keep in touch then.”
[Relationship Increased by 4""")
          #lana_dialoguecomplete2 += 1
        #elif lana_dialoguecomplete2 == 1:
          #print("Lana already felt comfortable to talk to you about that.")
      elif lanaconvo_1 == "e":
          print("You leave.")
          break
    elif lana_pickconvo == 2:
      print(textwrap.dedent("""A: Talk about aspirations
B: Talk about books
C: Talk about hobbies
D: Talk about TV
E: Leave"""))
      lanaconvo_2 = input("choose: ")
      if lanaconvo_2 == "a":
          print("""You ask Lana if she has aspirations for the future.
She says she would like to be an illustrator.
[Relationship Increased by 1]""")
          profiles.Lana.level += 1
      elif lanaconvo_2 == "b":
          print("""You ask Lana about any books she has read.
She talks about one book where high school students pilot mech robots.
[Relationship Increased by 1]""")
          profiles.Lana.level += 1
      elif lanaconvo_2 == "c":
          print("""You ask Lana about hobbies she has.
She says she likes art, writing and video games.
[No Relationship Gain]""")
      elif lanaconvo_2 == "d":
          print("""You ask Lana about any shows she's watched.
She talks about a show where teenagers solve mysteries.
[Relationship Increased by 1]""")
          profiles.Lana.level += 1
      elif lanaconvo_2 == "e":
          print("You leave.")
          break


  # Sid Convo
def sidconvo():
    sid_pickconvo = random.randint(0, 2)
    print("You talk to Sid.")
    if sid_pickconvo == 0:
      print("""A: Talk about school
B: Talk about work
C: Talk about romance
D: Talk about TV""")
      sidconvo_0 = input("choose: ")
      if sidconvo_0 == "a":
        print("""You discuss school with Sid.
He complains about the larger workload,
while talking about how he doesn’t like the teachers.
[Relationship Increased by 1]""")
        profiles.Sid.level += 1
      elif sidconvo_0 == "b":
        print("""You ask if Sid has been looking at any jobs.
He states that he’s been applying everywhere, but hasn’t had any luck.
[No Relationship Gain]""")
      elif sidconvo_0 == "c":
        print("""You ask Sid if he’s had any luck with the ladies. 
He slyly smirks at you.
[Relationship Increased by 1]""")
        profiles.Sid.level += 1
      elif sidconvo_0 == "d":
        print("""You ask Sid about any shows he’s watched. 
He talks about this one show where 4 guys in New York compete 
to pull jokes on people in public. 
[Relationship Increased by 1]""")
        profiles.Sid.level += 1
    elif sid_pickconvo == 1:
      print("""A: Talk about gossip
B: Talk about jokes
C: Talk about family
D: Talk about old friends""")
      sidconvo_1 = input("choose: ")
      if sidconvo_1 == "a":
        print("""You ask if Sid has heard any rumors going around. 
He says that he’s heard a rumor that some kids have been jumping into TVs. 
You aren’t quite sure if he’s being honest or not.
[No Relationship Gain]""")
      elif sidconvo_1 == "b":
        print("""You ask Sid about any jokes he’s heard. 
He tells you a joke about a chicken crossing the road. 
Said chicken gets run over by a semi-truck. 
[Relationship Increased by 1]""")
        profiles.Sid.level += 1
      elif sidconvo_1 == "c":
        print("""You discuss family with Sid.
He says that his parents left town for a “business trip”.
He seems excited to have the whole house to himself.
[Relationship Increased by 1]""")
        profiles.Sid.level += 1
      elif sidconvo_1 == "d":
        print("""You ask Sid about anyone from elementary school. 
He talks about this one girl who started her own punk rock band.
[No Relationship Gain]""")


  # Connor Convo
def connorconvo():
  connor_pickconvo = random.randint(0, 2)
  print("You walk over and talk to Connor.")
  while True:
    if connor_pickconvo == 0:
        print("""A: Talk about school
B: Talk about jobs
C: Talk about sports
D: Talk about TV
E: Leave""")
        connorconvo_0 = input("Choose: ")
        if connorconvo_0 == "a":
          print("""You talk about school with Connor. 
He says that he’s been more focused on sports,
but has been trying to make time for other things. 
[No Relationship Gain]""")
        elif connorconvo_0 == "b":
          print("""You ask if Connor has been looking for any jobs. 
He says he doesn’t have the time to find one.
[No Relationship Gain]""")
        elif connorconvo_0 == "c":
            print("""You ask Connor how the school sports are going.
He says that both teams have been practicing a lot more than they usually do. 
[Relationship Increased by 1]""")
            profiles.Connor.level += 1
        elif connorconvo_0 == "d":
          if profiles.Connor.level <= 10:
            print("""You ask Connor what sorts of shows he watches. 
He sighs.
You may need to grow closer before talking about this.
[Relationship Decreased by 1]""")
            profiles.Connor.level -= 1
          elif profiles.Connor.level >= 10:
            print("""You ask Connor what shows he watches. He sighs.
“I would watch TV, but my dad says it’s a ‘distraction’. 
It’s like he hates me having hobbies.”
He looks defeated.
“Oh, sorry about going off the cuff like that. 
I don’t usually talk about my family. Especially my dad.”
[Relationship Increased by 4]""")
            
        elif connorconvo_0 == "e":
          print("You leave.")
          break
    elif connor_pickconvo == 1:
      print("""A: Talk about homework
B: Talk about local events
C: Talk about gossip
D: Talk about family""")
      lanaconvo_1 = input("choose: ")
      if lanaconvo_1 == "a":
        print("""You talk about some homework you have been assigned.
She seems sympathetic but uninterested.
[No Relationship Gain]""")
      elif lanaconvo_1 == "b":
        print("""You talk about an event that’s happening soon. 
Lana seems somewhat curious.
[Relationship Increased by 1]""")
        profiles.Lana.level += 1
      elif lanaconvo_1 == "c":
        print("""You ask Lana if she’s heard any gossip around school.
She does mention that she heard rumors about a couple that split up recently.
[No Relationship Gain]""")
      elif lanaconvo_1 == "d":
        if profiles.Lana.level <= 15:
          print("""You try to talk about your family,
but Lana seems a bit down when you mention it.
You may need to grow closer before talking about this.
[Relationship Decreased by 1]""")
          profiles.Lana.level -= 1
        elif profiles.Lana.level >= 15:
          print("""You talk about your family, 
and Lana looks at you, then speaks:
“I wish my family was like that. My dad is usually too drunk to stand. 
He yells a lot, too…”
She looks down at the floor.
“Hopefully, I can move out one day. Do my own thing. That’d be nice.”
She looks at you again.
“Maybe we can still keep in touch then.”
[Relationship Increased by 4""")
    elif lana_pickconvo == 2:
      print("""A: Talk about aspirations
B: Talk about books
C: Talk about hobbies
D: Talk about TV""")
      lanaconvo_2 = input("choose: ")
      if lanaconvo_2 == "a":
        print("""You ask Lana if she has aspirations for the future.
She says she would like to be an illustrator.
[Relationship Increased by 1]""")
        profiles.Lana.level += 1
      elif lanaconvo_2 == "b":
        print("""You ask Lana about any books she has read.
She talks about one book where high school students pilot mech robots.
[Relationship Increased by 1]""")
        profiles.Lana.level += 1
      elif lanaconvo_2 == "c":
        print("""You ask Lana about hobbies she has.
She says she likes art, writing and video games.
[No Relationship Gain]""")
      elif lanaconvo_2 == "d":
        print("""You ask Lana about any shows she's watched.
She talks about a show where teenagers solve mysteries.
[Relationship Increased by 1]""")
        profiles.Lana.level += 1


  # Stephen Convo
def stephenconvo():
  jgjgjhh
  
  # Game Over (Below 0)