import random as rnd

class Ground:
    def size(self):
        inp = self
        ground = []
        for i in range (inp):
            ground.append(['~']*inp)

        return ground

    def input_size(self):
        if self>=5:
            return self



def place_ships(ships,ground):
    count = 0
    size=len(ground[0])-1
    while count != ships:
        x = rnd.randint(0, size)
        y = rnd.randint(0, size)
        ground[y][x] = 'o'
        count += 1
    return ground

def shot(x,y,ground_final, displayed):
    if ground_final[y][x] == 'o':
        print('Hit!')
        displayed[y][x] = 'X'
    else:
        print ('We missed!')
        displayed[y][x] = '*'


def to_1Dnify(list):
    list1D = []
    for i in list:
        for j in i:
            list1D.append(j)
    return list1D
