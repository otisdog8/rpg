class game:
    """Starts the game, coordinates menus, fighting, turns, ect, ect"""
    def __init__(self):
        self.savemanager = self.importer('savemanagement')
        self.player = self.importer('player')
        try:
            savefile = open("savefile.txt",'r')
            savefile.close()
            savefileexists = True
        except:
            savefileexists = False
        self.start(savefileexists)

    def start(self,savefileexists):
        if savefileexists == False:
            self.save = self.savemanager.nosave()
        elif savefileexists == True:
            self.save = self.savemanager.opensave()
        else:
            print("This is am impossible error")
        self.player.getstats(self.save)
    def importer(self,module):
        output = __import__(module)
        return output.add()
game()
