#This allows my custom import method to find the class
def add():
    return player()
class player():
    """The main player class; handles things like stats, and is one of the classes involved with fighting."""
    def __init__(self):
        import math
        import random
        self.random = random
        self.math = math
    def getstats(self,stats): #This gives me all the stats I need to live a happy, fuffilling life
        self.endurance = stats[0]
        self.strength = stats[1]
        self.xp = stats[2]
        self.hp = stats[3]
        self.maxhp = self.endurance * 10
        self.level = self.math.floor(float(self.xp/100))
        self.totalstats = self.level*5+20
    def heal(self): #Heals the character
        self.hp = self.hp + self.endurance
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        else:
            pass
    def startfight(self): #The main fight loop
        self.enemy = self.importer('enemy')
        self.enemy.create(self.level)
    def fight(self):
        enemyfight = self.enemy.fight(self.strength)
        if enemyfight[0] >= 0:
            print('You won')
        else:
            print('You took ' + str(enemyfight[1] + self.random.randint(0,enemyfight[1])-self.endurance/2) + 'damage.')
            self.hp = self.hp - (enemyfight[1] + self.random.randint(0,enemyfight[1])-self.endurance/2)
            if self.hp <= 0:
                print('You lost')
            else:
                self.fight()
            self.fight()
    def importer(self,module): #My custom import method
        output = __import__(module)
        return output.add()
