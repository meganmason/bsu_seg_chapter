# monica and megan climbing class

class climbing:
    def __init__(self, location, rock, height, grade):
        self.location = location
        self.rock = rock
        self.height = height
        self.grade = grade


    def pitches(self):

        pitches = self.height/100 #170 m rope length

    #def hours(self):
        #num_hours = pitches * (grade-5)



site1 = climbing("yosemite","granite", 3000, 5.11)
print('location',site1.location)
print('number of pitches',site1.pitches())
#print(site1.hours)

site2 = climbing("red river gorge","sandstone", 100, 5.14)
print('location',site2.location)
print(site2.pitches())
#print(site2.hours())

site3 = climbing("black cliffs","basalt", 50, 5.6)
print('location',site3.location)
print(site3.pitches())
#print(site3.hours())
