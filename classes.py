import profiles

# Defs For Each Of The Classes
  # Art
def attendart():
  if profiles.lana.intro == 0:
    print("You attend the class.")
  if profiles.Lana.intro == 1:
    profiles.Lana.level += 2
    print("""By showing interest in Lana's favorite class, you grew closer. 
[Relationship Increased By 2]""")
  # Social
def attendsocial():
  if profiles.Lana.intro == 0:
    print("You attend the class.")
  if profiles.Lana.intro == 1:
    profiles.Lana.level += 1
    print("""Though reluctant to accept your help, Lana learned from you.
[Relationship Increased By 1]""")
  # Science
def attendscience():
  if profiles.Stephen.intro == 0:
    print("You attend the class.")
  elif profiles.Stephen.intro == 1:
    profiles.Stephen.level += 0
    print(""""You try to spend time with Stephen but he is too busy with a personal experiment.
[Relationship Did Not Increase]""")
  # Ela
def attendela():
  if profiles.Lana.intro == 0:
    print("You attend the class.")
  elif profiles.Lana.intro == 1:
    profiles.Lana.level += 1
    profiles.Sid.level += 4
    print("""You and Sid convinced Lana to join you for a short homework session after class.
[Lana Relationship Increaded By 1]
[Sid Relationship Increased By 4]""")
  # Gym
def attendgym():
  if profiles.Connor.intro == 0:
    print("You attend the class.")
  elif profiles.Connor.intro == 1:
    profiles.Connor.level += 2
    print("""You, Connor and a few other students play basketball.
Luckily you were on a team with Connor.
You and Connor dominated the court.
[Relationship with Connor Increased By 2]""")
  # Pool
def attendpool():
  profiles.Sid.level += 2
  print("""You and Sid have a few races in the pool.
He beat you 4 - 0.
[Relationship Increased By 2]
[Pride Decreased By 999]""")
  # Track
def attendtrack():
  if profiles.Connor.level == 0:
    print("You attend the class.")
  elif profiles.Stephen.level == 0:
    print("You attend the class.")
  else:
    profiles.Connor.level += 5
    profiles.Stephen.level -= 2
    print("""You and Connor try to cheer Stephen on as he runs around the track.
Connor and you had fun but Stephen was too exhausted to even talk.
[Stephen Relationship Decreased By 2]
[Connor Relationship Increased By 5]""")
  # Math
def attendmath():
  profiles.Connor.level += 3
  print("""Connor, to your surprise, was intensly listening to the lesson.
By helping him with the parts he didint understand, you grew closer.
[Relatinship Increased By 3""")
  # Club
def attendclub():
  if profiles.Lana.intro == 0:
    print("You attend the class.")
  elif profiles.Lana.intro == 1:
    profiles.Sid.level -= 4
    profiles.Lana.level += 2
    print("""Sid sat bored out of his mind while you and Lana help the drama club paint posters for the upcoming play.
[Relationship With Sid Decreased By 4]
[Relationship With Lana Increased By 2]""")