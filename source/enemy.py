def add():
    return enemy()
class enemy:
    def __init__(self):
        import random
        self.random = random
    def create(self,level):
        self.endurance = self.random.randint(0,((level+4)*4))
        self.strength = (level+4)*4-self.endurance
        self.hp = self.endurance*10
    def fight(self,damage):
        self.hp = self.hp - (damage + self.random.randint(0,damage/2)-self.endurance/2)
        print('Enemy took ' + str(damage + self.random.randint(0,damage/2)-self.endurance/2) + 'damage.')
        return self.hp,self.Strength
