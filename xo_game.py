import sys

def CheckFull():
    check = 0
    for i in borad:
        for ii in i:
            check += ii
    return True if check == 45 or check == 54 else False

def CheckWin():
    status = (False,None)
    for i in borad: # vertical_check
        if sum(i) == 3:
            status = (True,1)
        elif sum(i) == 30:
            status = (True,10)
    check = [[0,0,0],[0,0]]
    for p in range(len(borad)): # horizontal_check and oblique_check
        for pp in range(len(borad[p])):
            check[0][pp] += borad[p][pp]
            if p == pp:
                check[1][0] += borad[p][pp]
            if p + pp == 2:
                check[1][1] += borad[p][pp]
    for k in check:
        for kk in k:
            if kk == 3:
                status = (True,1)
            elif kk == 30:
                status = (True,10)
    return status
def PrintBorad():
    print(' _ _ _ ')
    for l in borad:
        print('|',end='')
        for ll in l:
            if ll == 0:
                print(' ',end='')
            elif ll == 1:
                print('O',end='')
            else:
                print('X',end='')
            print('|',end='')
        # print('\n')
        print('\n - - - ')

borad = [[0,0,0],[0,0,0],[0,0,0]]
p = [None,None]
p[0] = input('Enter (1) X or (2) Y for P1: ')
while int(p[0]) != 1 and int(p[0]) != 2:
    p[0] = input('Enter (1) X or (2) Y for P1: ')
if int(p[0]) == 1:
    p[0] = 10 # x
    p[1] = 1 # o
    print('P1 is X')
    print('P2 is O')
elif int(p[0]) == 2:
    p[0] = 1 # o
    p[1] = 10 # x
    print('P1 is O')
    print('P2 is X')

state = input('Choose first player: (1)P1 or (2)P2: ')
while int(state) != 1 and int(state) != 2:
    state = input('Choose first player: (1)P1 or (2)P2: ')
print(f'P{state} first play!')
PrintBorad()
while not CheckFull() and CheckWin()[0] != True :
    row,column = input(f'P{state} Choose index of borad... (row,column) ex. 1 2: ').split(' ')
    while borad[int(row)][int(column)] == 1 or borad[int(row)][int(column)] == 10:
        row,column = input(f'Try Again! P{state} Choose index of borad... (row,column) ex. 1 2: ').split(' ')
    borad[int(row)][int(column)] = p[int(state)-1]
    PrintBorad()
    status = CheckWin()
    if status[0]:
        print('Player 1 Win!!!!!!') if p[0] == status[1] else print('Player 2 Win!!!!!!')
        sys.exit()
    state = '1' if state == '2' else '2'
    print('\n')
print('Draw!')

    