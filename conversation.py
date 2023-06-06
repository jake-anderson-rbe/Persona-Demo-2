# Imports
import profiles
import random
Rooms = ("Talk", "Attend Class", "Leave")



# Only used block comments for Lana, since same code
# applies to rest of characters

# Conversation Code
# Lana Convo
def lanaconvo():
    """Code defined for when you have a conversation with Lana"""
    # Randomly picks from 3 different "conversations" to be used
    # in an interaction
    lana_pickconvo = random.randint(0, 2)
    print("You walk over and talk to Lana.")
    while True:
        # If the value 0 is picked, this code will run:
        if lana_pickconvo == 0:
            print("""A: Talk about art
B: Talk about school
C: Talk about home
D: Talk about video games
E: Leave""")
            # Defines console input for choosing options
            lanacount_0 = input("Choose: ")
            if lanacount_0.lower() == "a":
                print("""You discuss art with Lana. 
You think you could learn some art techniques from her… 
[Relationship Increased by 1]""")
                profiles.Lana.level += 1
                break
                  
            elif lanacount_0.lower() == "b":
                print("""You talk about how school is going. 
Lana seems like she is barely listening.
[No Relationship Gain]""")
                break
            elif lanacount_0.lower() == "c":
                # If you are under the required relationship level, this will print:
                if profiles.Lana.level <= 10:
                    print("""You try to talk about your home life, 
but Lana shoots you a glare.
You may need to grow closer before talking about this.
[Relationship Decreased by 1]""")
                    profiles.Lana.level -= 1
                    break
                # If you are over the required relationship level, this will print:
                elif profiles.Lana.level >= 10:
                    print('''You ask Lana about her home life. 
She sighs.
“I dunno. My parents aren’t the best.
They all seem so focused on work and whatever new fad they’ve found.
Usually, it’s like I’m a ghost to them. Like I don’t exist.”
She sighs again, before looking up at you.
“Oh, uh, I didn’t mean to get all that depressing.”
She laughs to herself, and looks at you.
“Either way, thanks for listening. I needed to get that off my chest.”
[Relationship Increased by 4]''')
                    profiles.Lana.level += 4
                        # When finished, this value goes up by 1
                        # This is so players can't reuse unlocked conversations
                        # to get a lot of relationship levels very quickly
                    profiles.lana_dialoguecomplete1 += 1
                    break
                elif profiles.lana_dialoguecomplete1 == 1:
                    print("Lana already felt comfortable to talk to you about that.")
            elif lanacount_0.lower() == "d":
                print("""You talk about a new game that came out. 
Lana seems interested.
[Relationship Increased by 1]""")
                profiles.Lana.level += 1
                break
            elif lanacount_0.lower() == "e":
                # Lets you leave, and sends you back to the menu
                print("You leave.")
                break
            else:
                print("Invalid input!")
          
        elif lana_pickconvo == 1:
            # If the value 1 is picked, this will print:
            print("""A: Talk about homework
B: Talk about local events
C: Talk about gossip
D: Talk about family
E: Leave""")
            lanaconvo_1 = input("Choose: ")
            if lanaconvo_1.lower() == "a":
                print("""You talk about some homework you have been assigned.
She seems sympathetic but uninterested.
[No Relationship Gain]""")
                break
            elif lanaconvo_1.lower() == "b":
                print("""You talk about an event that’s happening soon. 
Lana seems somewhat curious.
[Relationship Increased by 1]""")
                profiles.Lana.level += 1
                break
            elif lanaconvo_1.lower() == "c":
                print("""You ask Lana if she’s heard any gossip around school.
She does mention that she heard rumors about a couple that split up recently.
[No Relationship Gain]""")
                break
            elif lanaconvo_1.lower() == "d":
                if profiles.Lana.level <= 15:
                    print("""You try to talk about your family,
but Lana seems a bit down when you mention it.
You may need to grow closer before talking about this.
[Relationship Decreased by 1]""")
                    profiles.Lana.level -= 1
                    break
                elif profiles.Lana.level >= 15:
                    print('''You talk about your family, 
and Lana looks at you, then speaks:
“I wish my family was like that. My dad is usually too drunk to stand. 
He yells a lot, too…”
She looks down at the floor.
“Hopefully, I can move out one day. Do my own thing. That’d be nice.”
She looks at you again.
“Maybe we can still keep in touch then.”
[Relationship Increased by 4''')
                    profiles.Lana.level += 4
                    profiles.lana_dialoguecomplete2 += 1
                    break
                elif profiles.lana_dialoguecomplete2 == 1:
                    print("Lana already felt comfortable to talk to you about that.")
            elif lanaconvo_1.lower() == "e":
                print("You leave.")
                break
            else:
                print("Invalid input!")
        
        elif lana_pickconvo == 2:
            # If the value 2 is picked, this will print:
            print("""A: Talk about aspirations
B: Talk about books
C: Talk about hobbies
D: Talk about TV
E: Leave""")
            lanaconvo_2 = input("Choose: ")
            if lanaconvo_2.lower() == "a":
                print("""You ask Lana if she has aspirations for the future.
She says she would like to be an illustrator.
[Relationship Increased by 1]""")
                profiles.Lana.level += 1
                break
            elif lanaconvo_2.lower() == "b":
                print("""You ask Lana about any books she has read.
She talks about one book where high school students pilot mech robots.
[Relationship Increased by 1]""")
                profiles.Lana.level += 1
                break
            elif lanaconvo_2.lower() == "c":
                print("""You ask Lana about hobbies she has.
She says she likes art, writing and video games.
[No Relationship Gain]""")
                break
            elif lanaconvo_2.lower() == "d":
                print("""You ask Lana about any shows she's watched.
She talks about a show where teenagers solve mysteries.
[Relationship Increased by 1]""")
                profiles.Lana.level += 1
                break
            elif lanaconvo_2.lower() == "e":
                print("You leave.")
                break
            else:
                print("Invalid input!")


  # Sid Conversation
def sidconvo():
    sid_pickconvo = random.randint(0, 1)
    print("You walk over and talk to Sid.")
  
    while True:
        if sid_pickconvo == 0:
            # If 0 is picked, this will print:
            print("""A: Talk about school
    B: Talk about work
    C: Talk about romance
    D: Talk about TV""")
            sidconvo_0 = input("Choose: ")
            if sidconvo_0.lower() == "a":
                print("""You discuss school with Sid.
He complains about the larger workload,
while talking about how he doesn’t like the teachers.
[Relationship Increased by 1]""")
                profiles.Sid.level += 1
                break
            elif sidconvo_0.lower() == "b":
                print("""You ask if Sid has been looking at any jobs.
He states that he’s been applying everywhere, but hasn’t had any luck.
[No Relationship Gain]""")
                break
            elif sidconvo_0.lower() == "c":
                print("""You ask Sid if he’s had any luck with the ladies. 
He slyly smirks at you.
[Relationship Increased by 1]""")
                profiles.Sid.level += 1
                break
            elif sidconvo_0.lower() == "d":
                print("""You ask Sid about any shows he’s watched. 
He talks about this one show where 4 guys in New York compete 
to pull jokes on people in public. 
[Relationship Increased by 1]""")
                profiles.Sid.level += 1
                break
            else:
                print("Invalid input!")
            
        elif sid_pickconvo == 1:
            # If the value 1 is picked, this will print:
            print("""A: Talk about gossip
B: Talk about jokes
C: Talk about family
D: Talk about old friends""")
            sidconvo_1 = input("Choose: ")
            if sidconvo_1.lower() == "a":
                print("""You ask if Sid has heard any rumors going around. 
He says that he’s heard a rumor that some kids have been jumping into TVs. 
You aren’t quite sure if he’s being honest or not.
[No Relationship Gain]""")
                break
            elif sidconvo_1.lower() == "b":
                print("""You ask Sid about any jokes he’s heard. 
He tells you a joke about a chicken crossing the road. 
Said chicken gets run over by a semi-truck. 
[Relationship Increased by 1]""")
                break
                profiles.Sid.level += 1
            elif sidconvo_1.lower() == "c":
                print("""You discuss family with Sid.
He says that his parents left town for a “business trip”.
He seems excited to have the whole house to himself.
[Relationship Increased by 1]""")
                break
                profiles.Sid.level += 1
            elif sidconvo_1.lower() == "d":
                print("""You ask Sid about anyone from elementary school. 
He talks about this one girl who started her own punk rock band.
[No Relationship Gain]""")
                break
            elif sidconvo_1.lower() == "e":
                print("You leave.")
                break
            else:
                print("Invalid input!")


  # Connor Convo
def connorconvo():
    connor_pickconvo = random.randint(0, 2)
    print("You walk over and talk to Connor.")
  
    while True:
        if connor_pickconvo == 0:
            # If the value 0 is picked, this will print:
            print("""A: Talk about school
B: Talk about jobs
C: Talk about sports
D: Talk about TV
E: Leave""")
            connorconvo_0 = input("Choose: ")
            if connorconvo_0.lower() == "a":
                print("""You talk about school with Connor. 
He says that he’s been more focused on sports,
but has been trying to make time for other things. 
[No Relationship Gain]""")
                break
            elif connorconvo_0.lower() == "b":
                print("""You ask if Connor has been looking for any jobs. 
He says he doesn’t have the time to find one.
[No Relationship Gain]""")
                break
            elif connorconvo_0.lower() == "c":
                print("""You ask Connor how the school sports are going.
He says that both teams have been practicing a lot more than they usually do. 
[Relationship Increased by 1]""")
                profiles.Connor.level += 1
                break
            elif connorconvo_0.lower() == "d":
                if profiles.Connor.level <= 10:
                    print("""You ask Connor what sorts of shows he watches. 
He sighs.
You may need to grow closer before talking about this.
[Relationship Decreased by 1]""")
                    profiles.Connor.level -= 1
                    break
                elif profiles.Connor.level >= 10:
                    print('''You ask Connor what shows he watches. He sighs.
“I would watch TV, but my dad says it’s a ‘distraction’. 
It’s like he hates me having hobbies.”
He looks defeated.
“Oh, sorry about going off the cuff like that. 
I don’t usually talk about my family. Especially my dad.“
[Relationship Increased by 4]''')
                    profiles.Connor.level += 4
                    profiles.connor_dialoguecomplete1 += 1
                    break
                elif profiles.lana_dialoguecomplete1 == 1:
                    print("Connor already felt comfortable to talk to you about that.")
            elif connorconvo_0.lower() == "e":
                print("You leave.")
                break
            else:
                print("Invalid input!")
          
        elif connor_pickconvo == 1:
            # # If the value 1 is picked, this will print:
            print("""A: Talk about homework
B: Talk about family
C: Talk about romance
D: Talk about video games
E: Leave""")
            connorconvo_1 = input("Choose: ")
            if connorconvo_1.lower() == "a":
                print("""You ask Connor about any homework he has. 
He says that he’s finished his ELA and Math homework, 
but hasn’t had time for anything else.
[No Relationship Gain]""")
                break
            elif connorconvo_1.lower() == "b":
                if profiles.Connor.level <= 15:
                    print("""You ask Connor about his family. 
He retorts with “what about them?”
You may need to grow closer before talking about this.
[Relationship Decreased by 1]""")
                    profiles.Connor.level -= 1
                    break
                elif profiles.Connor.level >= 15:
                    print('''You ask Connor about his family. He responds:
“I mean, yeah, they’re cool. I guess. My dad is a bit of a control freak, 
though. He goes on and on about me being the ‘star athlete’ and 
going on to play in the NFL or something. 
It feels like he hasn’t moved on from high school, 
and is just reliving it through me and my accomplishments.”
He sighs.
“I know I probably shouldn’t be talking about my dad like that. 
But, what can you do, y’know? 
Maybe I can be a writer one day, instead of doing sports.”
[Relationship Increased by 4]''')
                    profiles.Connor.level += 4
                    profiles.connor_dialoguecomplete2 += 1
                    break
                elif profiles.connor_dialoguecomplete2 == 1:
                    print("Connor already felt comfortable to talk to you about that.")
            elif connorconvo_1.lower() == "c":
                if profiles.Connor.level <= 20:
                    print("""You ask Connor how he’s been doing romantically. 
He doesn’t really know how to answer that question.
You may need to grow closer before talking about this.
[Relationship Decreased by 1]""")
                    profiles.Connor.level -= 1
                    break
                elif profiles.Connor.level >= 20:
                    print('''You ask Connor how he’s been doing romantically. 
He gives you a nervous look.
“I haven’t really told anyone about this, but… I think I might be gay. 
It’s made finding someone pretty hard. 
I know my dad would kill me if he knew.”
He nervously laughs.
“Sorry if that comes off as me asking you out on a date or something.
I don’t know which way your flag flies, so I don’t wanna pressure you.
Anyways, thanks for letting me talk. Feels like a weight off my shoulders.”
[Relationship Increased by 4]''')
                    profiles.Connor.level += 4
                    profiles.connor_dialoguecomplete3 += 1
                    break
                elif profiles.connor_dialoguecomplete3 == 1:
                    print("Connor already felt comfortable to talk to you about that.")
            elif connorconvo_1.lower() == "d":
                print("""You ask if Connor has played any video games lately.
He says he hasn’t had the time to play any.
[No Relationship Gain]""")
                break
            elif connorconvo_1.lower() == "e":
                print("You leave.")
                break
            else:
                print("Invalid input!")
          
        elif connor_pickconvo == 2:
            # If the value 2 is picked, this will print:
            print("""A: Talk about burnout
B: Talk about football
C: Talk about hobbies
D: Talk about local events
E: Leave""")
            connorconvo_2 = input("Choose: ")
            if connorconvo_2.lower() == "a":
                print("""You ask Connor if he’s been feeling 
burnt out with all the work he’s doing. 
He sighs, but nods.
[No Relationship Gain]""")
                break
            elif connorconvo_2.lower() == "b":
                print("""You ask Connor about the football game. 
He says that the deadline for the game is coming pretty soon, 
and he’s really focusing hard on it. 
[Relationship Increased by 1]""")
                break
                profiles.Connor.level += 1
            elif connorconvo_2.lower() == "c":
                print("""You ask Connor about any hobbies he has. 
He says he’s been dabbling in creative writing, 
and has been working on his own story.
[Relationship Increased by 1]""")
                profiles.Connor.level += 1
                break
            elif connorconvo_2.lower() == "d":
                print("""You ask Connor if he’s going to any local events. 
    He says that he wishes he could, but can’t.
    [No Relationship Gain]""")
                break
            elif connorconvo_2.lower() == "e":
                print("You leave.")
                break


  # Stephen Convo
def stephenconvo():
    print("You walk over and talk to Stephen.")
    stephen_pickconvo = random.randint(0, 2)
    
    while True: 
        if stephen_pickconvo == 0:
          # If the value 0 is picked, this will print:
            print("""A: Talk about math
B: Talk about gossip
C: Talk about art
D: Talk about interests
E: Leave""")
            stephenconvo_0 = input("Choose: ")
            if stephenconvo_0.lower() == "a":
                print("""You ask Stephen if math is going well. 
He gives you a thumbs up.
[Relationship Increased by 1]""")
                profiles.Stephen.level += 1
                break
            elif stephenconvo_0.lower() == "b":
                print("""You ask Stephen if he’s heard any gossip around the school.
He says he hasn’t heard anything. 
[No Relationship Gain]""")
                break
            elif stephenconvo_0.lower() == "c":
                print("""You talk about art with Stephen. 
He says he only likes art made by Japanese artists.
[Relationship Increased by 1]""")
                profiles.Stephen.level += 1
                break
            elif stephenconvo_0.lower() == "d":
                print("""You ask Stephen about his interests. 
This conversation goes way longer than you thought it would.
[Relationship Increased by 1]""")
                profiles.Stephen.level += 1
                break
            elif stephenconvo_0.lower() == "e":
                print("You leave.")
                break
        elif stephen_pickconvo == 1:
              # If the value 1 is picked, this will print:
              print("""A: Ask for math help
        B: Talk about comics
        C: Talk about news
        D: Talk about local events
        E: Leave""")
              stephenconvo_1 = input("Choose: ")
              if stephenconvo_1.lower() == "a":
                if profiles.Stephen.level <= 10:
                    print("""You ask Stephen for some help with math homework. 
    He gives you an annoyed look.
    You may need to grow closer before talking about this.
    [Relationship Decreased by 1]""")
                    profiles.Stephen.level -= 1
                    break
                elif profiles.Stephen.level >= 10:
                    print('''You ask Stephen for some help with math homework.
  “Alright, since we’re on good terms, sure. I think I may be of some help.”
  He takes your backpack, and you start studying together. 
  Stephen seems really smart.
  [Relationship Increased by 4]''')
                    profiles.Stephen.level += 4
                    profiles.stephen_dialoguecomplete1 += 1
                    break
                elif profiles.stephen_dialoguecomplete1 == 1:
                    print("Stephen already felt comfortable to talk to you about that.")
              elif stephenconvo_1.lower() == "b":
                  print("""You ask Stephen if he likes any comics. 
He goes on and on about this one “manga” where 
a guy turns into a sword. 
[Relationship Increased by 1]""")
                  profiles.Stephen.level += 1
                  break
              elif stephenconvo_1.lower() == "c":
                  print("""You ask Stephen about any news lately. 
He says a new video game came out, 
and he waited in the middle of the night to get it first.
[No Relationship Gain]""")
                  break
              elif stephenconvo_1.lower() == "d":
                  print("""You ask Stephen if he’s heading to any events around town.
        He excitedly talks about a comic con coming up.
        [Relationship Increased by 1]""")
                  break
              elif stephenconvo_1.lower() == "e":
                  print("You leave.")
                  break
        elif stephen_pickconvo == 2:
            # If the value 2 is picked, this will print:
            print("""A: Talk about TV
B: Talk about movies
C: Talk about video games
D: Talk about weather
E: Leave""")
            stephenconvo_2 = input("Choose: ")
            if stephenconvo_2.lower() == "a":
                print("""You ask Stephen about any TV shows he watches. 
He says he only watches anime.
[Relationship Increased by 1]""")
                profiles.Stephen.level += 1
                break
            elif stephenconvo_2.lower() == "b":
                print("""You ask Stephen about any movies he’s watched. 
He talks about this adaptation of a comic he read, 
and how the movie was so much worse than the comic.  
[No Relationship Gain]""")
                break
            elif stephenconvo_2.lower() == "c":
                print("""You ask Stephen about any video games he’s played recently.
He gushes about this game where you get to date anime girls. 
[Relationship Increased by 1]""")
                profiles.Stephen.level += 1
                break
            elif stephenconvo_2.lower() == "d":
                print("""You ask Stephen about the weather. 
        He says he doesn’t really care, since he stays inside a lot.
        [No Relationship Gain]""")
                break
            elif stephenconvo_2.lower() == "e":
                print("You leave.")
                break