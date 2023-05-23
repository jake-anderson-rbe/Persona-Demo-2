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

Art = Rooms("Art", """
One of the smaller rooms in the school. 
Inorder to use this small space, students have moved the chairs and desks to the far side of the room.
in place of where these school essentials are stools and canvases.
""", 'Lana')
Math = Rooms("Math", """
A normal class room, that is if you look past all the students that are outwardly expressing their distane for this class.
""", "Connor")
Social = Rooms("Social", """
A medium sized class room.
A giant map of the world and a much smaller map of europe hang behind the teacher podium.
The students in this class are either chearfully talking to friends or furiously writing in notebooks, studying the maps.
""", "Lana")
ELA = Rooms("ELA", """
Unlike the other normal rooms, the ELA classroom is more of a lecture hall.
The students here all sit patiently and quietly while waiting for the teacher,
or they are struggling to get last minute work done.
""", "Sid, Lana")
Science = Rooms("Science", """
A normally sized room, but there are no chairs or desks.
instead, this room has six quartz tables that take up the centre of the room.
students prepair safety gear and start cleaning some of the messes the last class made.
""", "Stephen")
Track = Rooms("Track Field", """
A large 400m Track spans around a football field.
Not many students are here, but as for the ones who are, they sit on the bleachers or are runing around the track.
""", "Connor, Stephen")
Pool = Rooms("Pool", """
A 25 yard long pool takes up the inside of a glassroofed buildiung.
To no ones surprise, the students here are happily swimming or racing one another.
""", "Sid")
Gym = Rooms("Gym", """
A large building connected to the left of the school.
inside there are two basketball hoops on either side of the gym floor.
downstairs is an actual gym.
The students here are mostly doing stretches in preperation for the class.
""", "Connor")
Club = Rooms("Club Building", """
Small building dissconected from  the right side of the school.
This building is practically just a small school building, with classrooms and everything.
You would enter a classroom to see what the students are doing, but you dont want to disturb the clubs.
""", "Lana, Sid")


#class Outdoors:
  #def __init__(self, location, discription, character)