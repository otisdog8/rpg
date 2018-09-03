class game(object):
    """Starts the game, coordinates menus, fighting, turns, ect, ect"""
    def __init__(self, arg):
        super(game, self).__init__()
        self.arg = arg
        import menu
        #Check for existence of savefile
        try:
            #open savefile
            self.savefileexists = True
        except:
            self.savefileexists = False
        self.start(savefileexists)
    def start(savefileexists):
        pass
