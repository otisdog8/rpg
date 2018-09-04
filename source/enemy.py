def add():
    return enemy()
class enemy:
    def __init__(self):
        import random
        self.random = random
        endurance = random.randint(0,30)
        strength = 30 - endurance
