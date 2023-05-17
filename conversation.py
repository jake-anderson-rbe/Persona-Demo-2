def lanaone():
  print("O-Oh, hello. I dont really have much to say... Could you leave me alone?")
  options = ("1) Are you okay?", "2) Alright.", "3) Did I do somthing wrong?")
  print(f"{options}")
  option_input = input("\n?:")
  if option_input == "1":
    print("""
    Huh? I-I... I am okay.
    *People dont usually ask me that*
    I just dont know how to converse with others
    Now, could you Leave please?
    """)
  if option_input == "3":
    print("""
    No! Of course not! I... 
    I just dont know how to converse with others
    Now, could you Leave please?
    """)
  if option_input == "2":
    Travel()

def lanatwo():
  print("""
  I might need to look at another tutorial... should I shade this? 
  where is the light coming from? 
  Oh! I didnt see you... Um... please dont scare me like that.
  """)

def lanathree():
  print("""
  Could you not stare at me, please.
  Oh, you were looking at my painting.
  """)