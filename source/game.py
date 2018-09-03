class game:
    """Starts the game, coordinates menus, fighting, turns, ect, ect"""
    def __init__(self, arg):
        self.arg = arg
        import menu
        #Check for existence of savefile
        savefileexists = False
        try:
            self.savefileexists = True
        except:
            self.savefileexists = False
        self.start(savefileexists)
    def start(self,savefileexists):
        if savefileexists == False:
            pass
        elif savefileexists == True:
            pass
        else:
            print("This is am impossible error")
    
