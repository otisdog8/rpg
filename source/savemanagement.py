#This allows my custom import method to find the class
def add():
    return savemanager()
class savemanager:
    """Manages saves."""
    def __init__(self):
        pass
    def nosave(self):
        self.savefile = open('savefile.txt','a')
        self.savefile.write("10\n10\n0\n20\n20\n0\n100") #Endurance,Strength,Level,StatsSpent,StatsTotal,XP,HP
        self.savefile.close()
        return [10,10,0,20,20,0,100]
    def opensave(self):
        pass
    def modifysave(self):
        pass
