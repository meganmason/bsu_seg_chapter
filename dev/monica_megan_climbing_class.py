# monica and megan climbing class


#notes to improve (SEG meeting)
#defult values:
    def __init__(self, location='yosemite', rock='hard', height='1', grade='5.1'):
#on/off switches
    #*args/**kwargs

#GOALS
#import list of yose climbs and make table

class climbing:
    def __init__(self, location, rock, height, grade): #static method
        self.location = location
        self.rock = rock
        self.height = height
        self.grade = grade


    def pitches(self): #instance method - because pitches(self). if def pitches --static
        pitches = self.height/170 #170 m rope length
        return pitches # return self.pitches

    def hours(self):
        hours = self.pitches() * (self.grade-5)*2
        return hours



site1 = climbing("yosemite","granite", 3000, 5.11) #instance of class or object
print('location',site1.location)
print('number of pitches',site1.pitches())
print('hours to climb', site1.hours())

site2 = climbing("red river gorge","sandstone", 100, 5.14)
print('location',site2.location)
print('number of pitches',site2.pitches())
print('hours to climb', site2.hours())

site3 = climbing("black cliffs","basalt", 50, 5.6)
print('location',site3.location) #runs an attribue
print('number of pitches',site3.pitches()) #runs a method
print('hours to climb', site3.hours())
