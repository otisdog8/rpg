class game:
    """Starts the game, coordinates menus, fighting, turns, ect, ect"""
    def __init__(self):
        self.savemanager = self.importer('savemanagement') #imports my classes into the monolithic game class
        self.player = self.importer('player')
        self.menus = self.importer('menus')
        try:
            savefile = open("savefile.txt",'r') #tests for savefile
            savefile.close()
            savefileexists = True
        except:
            savefileexists = False
        self.start(savefileexists)
        response = self.menus.start()
        if response == '1':
            pass
        elif response == '2':
            self.save = self.savemanager.nosave() #If the player wants to reset this happens
            self.player.getstats(self.save)
        else:
            pass
        self.gameloop()
    def start(self,savefileexists): #Works with the save
        if savefileexists == False:
            self.save = self.savemanager.nosave()
        elif savefileexists == True:
            self.save = self.savemanager.opensave()
        else:
            print("This is am impossible error")
        self.player.getstats(self.save)
    def gameloop(self):
        while 1:
            self.player.startfight()
    def importer(self,module): #My custom import method
        output = __import__(module)
        return output.add()
game()
