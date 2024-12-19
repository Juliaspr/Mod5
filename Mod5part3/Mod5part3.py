import random
class Warrior:
    health = int()
    name = str
    endurance = int
    armor = int


    def __init__(self,name: str,  health:int, endurance:int, armor: int):
        self.health = health
        self.name = name
        self.armor = armor
        self.endurance = endurance

    def set_health(self, health:int):
        self.health = health

    def get_health(self):
        return self.health

    def set_armor(self, armor:int):
        self.armor = armor

    def get_armor(self):
        return self.armor

    def set_endurance(self, endurance:int):
        self.endurance = endurance

    def get_endurance(self):
        return self.endurance

    def defend(self):
        self.set_health(self.get_health() - random.randint(0, 10))
        self.set_armor(self.get_armor() - random.randint(0, 20))
        return self.health, self.armor


    def attack(self):
        self.endurance -= 10
        return self.endurance


if __name__ == '__main__':
    warrior1 = Warrior("A",  100, 100,100)
    warrior2 = Warrior("B",100,100,100)

    random_func = [warrior2.attack(), warrior2.defend(), warrior1.attack(), warrior1.defend()]
    while (warrior2.get_health()>0) and (warrior1.get_health()>0):
        
        print(random.choice(random_func))












