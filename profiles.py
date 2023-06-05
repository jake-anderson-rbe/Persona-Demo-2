class Character:
    def __init__(self, name, level, intro):
        self.name = name
        self.level = level
        self.intro = intro
Lana = Character("Lana", 0, 0)
Sid = Character("Sid", 0, 0)
Connor = Character("Connor", 0, 0)
Stephen = Character("Stephen", 0, 0)

# Dialogue Locks
# Lana:
lana_dialoguecomplete1 = 0
lana_dialoguecomplete2 = 0
# Connor:
connor_dialoguecomplete1 = 0
connor_dialoguecomplete2 = 0
connor_dialoguecomplete3 = 0
# Stephen:
stephen_dialoguecomplete1 = 0