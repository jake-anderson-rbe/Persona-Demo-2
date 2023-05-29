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
        print("“Oh, uh, I’m doing art, I guess.”")
        print("A: What are you painting?")
        print("B: I like it!")
        print("C: Guess it looks ok…")
        print("D: Leave\n")
        lana_introinput = input("Choose: ")
        if lana_introinput.lower() == "a":
            print("“Just a, uh, landscape.”")
        elif lana_introinput.lower() == "b":
            print("“Oh!”")
            print("""“I didn’t expect anyone would compliment my art…”
            A: What is your name?
            B: You like to paint?
            C: Where'd you learn to paint?""")
            lana_introinput = input("Choose: ")
            if lana_introinput.lower() == "a":
                print("“Uhm, it’s…Lana.”")
                print("“Anyways, I have some stuff I need to work on.”")
                print("You leave the room.")
                profiles.Lana.intro += 1
                break

            elif lana_introinput.lower() == "b":
                print("“Yeah, I do. It’s nice.”")
                print("“Anyways, I have some stuff I need to work on.”")
                print("You leave the room.")
                profiles.Lana.intro += 1
                break

            elif lana_introinput.lower() == "c":
                print("“Uh, I’d rather not say.”")
                print("“Anyways, I have some stuff I need to work on.”")
                print("You leave the room.")
                profiles.Lana.intro += 1
                break

        elif lana_introinput == "c":
            print("Yeah...")
            profiles.Lana.intro += 1
        elif lana_introinput == "d":
            print("ok")
    elif lana_introinput == "d":
      print("ok")
      break

