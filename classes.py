import conversation
import profiles

# Defs For Each Of The Classes
def attendart():
  if conversation.lanaIntroEnd.complete == 0:
    print("You attend the class.")
  if conversation.lanaIntroEnd.complete == 1:
    profiles.Lana.level += 2
    print("""By showing interest in Lana's favorite class, you grew closer. 
            [Relationship Increased By 2]""")
def attendsocial():
  if conversation.lanaIntroEnd.complete == 0:
    print("You attend the class.")
  if conversation.lanaIntroEnd.complete == 1:
    profiles.Lana.level += 1
    print("""Though reluctant to accept your help, Lana learned from you.
            [Relationship Increased By 1]""")
def attendscience():
  profiles.Stephen.level += 0
  print(""""You try to spend time with Stephen but he is too busy with a personal experiment.
            [Relationship Did Not Increase]""")
def attendela():
  profiles.Lana.level += 1
  profiles.Sid.level += 4
  print("""You and Sid convinced Lana to join you for a short homework session after class.
            [Lana Relationship Increaded By 1]
            [Sid Relationship Increased By 4]""")
def attendgym():
  profiles.Connor.level += 2
  print("""You, Connor and a few other students play basketball.
Luckily you were on a team with Connor.
You and Connor dominated the court.
            [Relationship with Connor Increased By 2]""")
def attendpool():
  profiles.Lana.level += 2
  print("""You and Sid have a few races in the pool.
He beat you 4 - 0.
            [Relationship Increased By 2]
            [Pride Decreased By 999]""")
def attendtrack():
  profiles.Connor.level += 5
  profiles.Stephen.level -= 2
  print("""You and Connor try to cheer Stephen on as he runs around the track.
Connor and you had fun but Stephen was to exhausted to even talk.
            [Stephen Relationship Decreased By 2]
            [Connor Relationship Increased By 5]""")
def attendmath():
  profiles.Connor.level += 3
  print("""Connor, to your surprise, was intensly listening to the lesson.
By helping him with the parts he didint understand, you grew closer.
            [Relatinship Increased By 3""")
def attendclub():
  profiles.Lana.level -= 4
  profiles.Lana.level += 2
  print("""Sid sat bored out of his mind while you and Lana help the drama club paint posters for the upcoming play.
            [Relationship With Sid Decreased By 4]
            [Relationship With Lana Increased By 2]""")

