#This allows my custom import method to find the class
def add():
    return player()
class player():
    """The main player class; handles things like stats, and is one of the classes involved with fighting."""
    def __init__(self):
        import math
        self.math = math
    def getstats(self,stats): #This gives me all the stats I need to live a happy, fuffilling life
        self.endurance = stats[0]
        self.strength = stats[1]
        self.xp = stats[2]
        self.hp = stats[3]
        self.maxhp = self.endurance * 10
        self.level = self.math.floor(float(self.xp/100))
        self.totalstats = self.level*5+20
    
