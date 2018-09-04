def add():
    return enemy()
class enemy:
    def __init__(self):
        pass
    def create(self,level):
        import random
        self.random = random
        self.endurance = random.randint(0,level*4)
        self.strength = level*4-endurance
        self.hp = self.endurance*10
    def fight(self,damage):
        pass
