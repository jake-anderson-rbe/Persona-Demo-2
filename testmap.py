school_locations = {"1st Floor", "2nd Floor", "Yard", "Roof"}
first_locations = {"Art", "Math", "Social"}
second_locations = {"ELA", "Science",}
yard_locations = {"Track Field", "Pool", "Gym", "Club Building"}

class FloorOne:
  def __init__(self, rooms):
    self.rooms

class Rooms:
  def __init__(self, lesson, discription, character):
    self.lesson = lesson
    self.discription = discription
    self.character = character

Art = Rooms('Art', 'Chairs moved to make room for multiple canvas', 'Lana')
Math = Rooms("Math", "packed room of unhappy students", "Connor")
Social = Rooms("Social", "Small room with a map beside the chalk board", "Lana")
ELA = Rooms("ELA", "Theater style seating room with giant chalkboard", "Sid, Lana")
Science = Rooms("Science", "Quartz tables, with lab equiptment on top", "Stephen")
Track = Rooms("Track Field", "A large four lane track field", "Connor, Stephen")
Pool = Rooms("Pool", "Decently sized pool fills the fenced off space", "Sid")
Gym = Rooms("Gym", "Large building connected to the left of the school", "Connor")
Club = Rooms("Club Building", "Small building dissconected from school", "Lana, Sid")


#class Outdoors:
  #def __init__(self, location, discription, character)