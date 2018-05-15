import numpy as np

####################################
##############solver################
def row_solver(myRow):
    if (np.count_nonzero(myRow==1) == 3):
        player = 1
    elif(np.count_nonzero(myRow==2) == 3):
        player = 2
    else:
        return
    print '\nPlayer' + str(player) + ' won!!!'
    Won = True
    return Won

def diagsSolver(bd):
    x = bd[0,0]==bd[1,1]==bd[2,2]
    y = bd[0,2]==bd[1,1]==bd[2,0]
    if x or y and (bd[1,1] != 0):
        print '\nPlayer' + str(bd[1,1]) + ' won!!!'
        Won = True
        return Won
    else:
        return


def solver(bd):
    for x in range(3):
        w = row_solver(bd[x,:])# checking for row
        w = row_solver(bd[:,x])# checking for column
    w = diagsSolver(bd)        # checking for diagonals
    for x in bd:
        print x
    return w

####################################
##############gamer################

def gamer(pos,bd,Turn):
    bd[(int(pos[0])-1),(int(pos[1])-1)] = Turn
    return bd
