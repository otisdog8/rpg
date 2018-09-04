#This allows my custom import method to find the class
def add():
    return savemanager()
class savemanager:
    """Manages saves."""
    def __init__(self):
        pass
    def nosave(self):
        savefile = open('savefile.txt','a')
        savefile.write("10\n10\n0\n100") #Endurance,Strength,StatsSpent,XP,HP
        savefile.close()
        return [10,10,0,100]
    def opensave(self):
        savefile = open('savefile.txt','r')
        savelines = savefile.readlines()
        output = []
        for l in savelines: #Converts to ints
            output.append(int(l))
        return output
    def modifysave(self):
        pass
