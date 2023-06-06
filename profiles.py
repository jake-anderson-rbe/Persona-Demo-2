class Character:
    """Class for defining character traits of each character"""
    # The "intro" attribute is used after a character's intro
    # is complete, so the intros won't repeat
    def __init__(self, name, level, intro):
        self.name = name
        self.level = level
        self.intro = intro

# Objects set for each of the characters
Lana = Character("Lana", 0, 0)
Sid = Character("Sid", 0, 0)
Connor = Character("Connor", 0, 0)
Stephen = Character("Stephen", 0, 0)

# Dialogue Locks

# When you use the locked conversation topics once,
# this value will increment. When the value equals
# 1, that topic will be unable to be used again

# Lana:
lana_dialoguecomplete1 = 0
lana_dialoguecomplete2 = 0
# Connor:
connor_dialoguecomplete1 = 0
connor_dialoguecomplete2 = 0
connor_dialoguecomplete3 = 0
# Stephen:
stephen_dialoguecomplete1 = 0

maxrelation = 25