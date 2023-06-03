class Character:
  def __init__(self, name, age, gender, level, description, intro):
    self.name = name
    self.age = age
    self.gender = gender
    self.level = level
    self.intro = intro
Lana = Character("Lana", "18", "Female", 0, """""", 0)
Sid = Character("Sid", "16", "Male", 0, """""", 0)
Connor = Character("Connor", "17", "Male", 0, """""", 0)
Stephen = Character("Stephen", "16", "Male", 0, """""", 0)

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