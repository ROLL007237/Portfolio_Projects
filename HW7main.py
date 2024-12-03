class Raspberry:
    stages = ['Absent', 'Flowering', 'Green', 'Red']
    def __init__(self, index=1,):
        self._index = index
        self._state = self.stages[0]

    def grow(self):
        x = self.stages.index(self._state)
        self._state = self.stages[x+1]

    def is_ripe(self):
        if self._state == 'Red':
            return True
        else:
            return False

class RaspberryBush:
    def __init__(self,amount=10):
        self._berries = [Raspberry(i) for i in range(amount)]
        self.amount = amount

    def grow_all(self):
        for i in range (len(self._berries)):
            if self._berries[i]._state != 'Red':
                self._berries[i].grow()

    def all_ripe(self):
        are_grown = [i.is_ripe() for i in self._berries]
        if all(are_grown):
            return True
        else: return False

    def give_all(self):
        self._berries = [Raspberry(i) for i in range(self.amount)]

class Human:
    def __init__(self, bush, name='Viktor Korneplod'):
        self.name = name
        self._plant = bush

    def work(self):
        self._plant.grow_all()
        berries()

    def harvest(self):
        if self._plant.all_ripe():
            self._plant.give_all()
        else: return print('Not all berries are ready :o')
    @staticmethod
    def knowledge_base():
        print('YO YO YO MY LITTLE GARDENER BRO\nDO U WANT TO GET SOME BERRIES? THAN MAKE THE GROWWWWWWW!!!!!\n')

bush = RaspberryBush(10)
human = Human(bush)
human.knowledge_base()

def berries():
    berries = [i._state for i in bush._berries]
    return print(berries)

if __name__ == '__main__':
    while True:
        act = int(input('Enter 1 to work, 2 for harvest'))
        if act == 1:
            human.work()
        if act == 2:
            human.harvest()
            berries()