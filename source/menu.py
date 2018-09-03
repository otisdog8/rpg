class menu:
    def __init__():
        try:
            self.save = file.open("save.txt",'a')
            self.save.close()
            self.fileexists = True
        except:
            pass
        
