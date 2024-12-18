class Warrior:
    health = int()
    name = str

    def __init__(self,name: str,  health:int):
        self.health = health
        self.name = name

    def set(self, health:int):
        self.health = health

    def get(self):
        return self.health

if __name__ == '__main__':
    warrior1 = Warrior("A",  100)
    warrior2 = Warrior("B",100)

    def hurt(warr1: Warrior, warr2: Warrior):
        if (warr1.get()>20):
            warr1.set(warr1.get() - 20)
            print("warrior: ", warr1.name, " was hurt, health: " ,warr1.get()," , warrior: ", warr2.name, " hit, health ", warr2.get() )
        else: print("warrior: " , warr2.name, " win")

    hurt(warrior2,warrior1)
    hurt(warrior1, warrior2)
    hurt(warrior2,warrior1)
    hurt(warrior1, warrior2)
    hurt(warrior2,warrior1)
    hurt(warrior1, warrior2)
    hurt(warrior1, warrior2)
    hurt(warrior1, warrior2)
    hurt(warrior1, warrior2)
    hurt(warrior1, warrior2)







