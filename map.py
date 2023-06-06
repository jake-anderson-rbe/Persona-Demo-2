# Map Locations
"""Dictionaries for all school locations"""
school_locations = {"1st Floor", "2nd Floor", "Yard", "Menu"}
first_locations = {"Art", "Math", "Social"}
second_locations = {"ELA", "Science",}
yard_locations = {"Track Field", "Pool", "Gym", "Club Building"}

class Rooms:
    def __init__(self, lesson, discription, character):
        """Class for defining each school location, and their character"""
        self.lesson = lesson
        self.discription = discription
        self.character = character

# Objects for each of the rooms
# Has room name, description, and character
Art = Rooms("Art", """
One of the smaller rooms in the school. 
In order to use this small space, 
students have moved the chairs and desks to the far side of the room,
and in place of where these school essentials would be are stools and canvases.
""", 'Lana')

Math = Rooms("Math", """
A normal classroom, that is if you look past all the students 
that are outwardly expressing their distain for this class.
""", "Connor")

Social = Rooms("Social", """
A medium sized classroom.
A giant map of the world and a much smaller map of 
Europe hang behind the teacher podium.
The students in this class are either cheerfully talking to friends
or furiously writing in notebooks, studying the maps.
""", "Lana")

ELA = Rooms("ELA", """
Unlike the other normal rooms, the ELA classroom is more of a lecture hall.
The students here all sit patiently and quietly while waiting for the teacher,
or they are struggling to get last minute work done.
""", "Sid and Lana")

Science = Rooms("Science", """
A normally sized room, but there are no chairs or desks.
Instead, this room has six quartz tables that take up the centre of the room.
Students prepare safety gear and start cleaning some of the messes
the last class made.
""", "Stephen")

Track = Rooms("Track Field", """
A large 400m track spans around a football field.
Not many students are here, but as for the ones who are, 
they sit on the bleachers or are running around the track.
""", "Connor and Stephen")

Pool = Rooms("Pool", """
A 25 yard long pool takes up the inside of a glassroofed buildiung.
To no ones surprise, the students here are happily swimming or racing one another.
""", "Sid")

Gym = Rooms("Gym", """
A large building connected to the left of the school.
Inside there are two basketball hoops on either side of the gym floor,
and downstairs is an actual gym.
The students here are mostly doing stretches in preparation for the class.
""", "Connor")

Club = Rooms("Club Building", """
Small building dissconected from the right side of the school.
This building is practically just a small school building, 
with classrooms and everything.
You would enter a classroom to see what the students are doing, 
but you dont want to disturb the clubs.
""", "Lana and Sid")