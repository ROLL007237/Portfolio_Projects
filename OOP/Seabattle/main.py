from lib import *
botflag = int(input('1 if bot 0 if person '))
inp=int(input('size of the field: '))

field = Ground.size(inp)
ships_inp = int(input('Choose a number of cells, occupied by ships '))
ground_final = place_ships(ships_inp,field)
player = []
for i in range (inp):
    player.append(['~']*inp)

if botflag == 0:
    while 'o' in to_1Dnify(ground_final):
        for line in player:
            print('  '.join(line))
        x,y = map(int, input('enter coordinates of fire (x y): ').split())
        shot(x,y,ground_final,player)
    else:
        print('You won!')
if botflag == 1:
    players_field = place_ships(ships_inp,Ground.size(inp))
    k=0
    while 'o' in to_1Dnify(ground_final) and 'o' in to_1Dnify(players_field):
        for line in players_field:
            print('  '.join(line))
        print()
        for line in player:
            print('  '.join(line))
        if k%2 == 0:
            x,y = map(int,input('Enter the fire coords (x y) : ').split())
            shot(x, y, ground_final, player)
        else:
            x,y = rnd.randint(0,inp-1), rnd.randint(0,inp-1)
            shot(x,y,players_field,players_field)
        k+=1
