class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print self.sounds[i % len(self.sounds)],
        print ""

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])
        
class Drummer(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Drummer, self).__init__(["Solo", "1, 2, 3, 4", "Spontaneously Combust", "Get Fired"])        

    def tune(self):
        print "Be with you in a moment"
        print "Twoning, sproing, splang"

    def solo(self, length):
        for i in range(length):
            print self.sounds[i % len(self.sounds)],
        print ""

nigel = Drummer()
nigel.solo(6)
print nigel.sounds
