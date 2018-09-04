class game:
    """Starts the game, coordinates menus, fighting, turns, ect, ect"""
    def __init__(self):
        self.savemanager = self.importer('savemanagement')
        try:
            savefile = open("savefile.txt",'r')
            savefile.close()
            self.savefileexists = True
        except:
            self.savefileexists = False
        self.start(self.savefileexists)

    def start(self,savefileexists):
        if savefileexists == False:
            self.save = self.savemanager.nosave()
            print(self.save)
        elif savefileexists == True:
            self.save = self.savemanager.opensave()
        else:
            print("This is am impossible error")
    def importer(self,module):
        output = __import__(module)
        return output.add()
game()
