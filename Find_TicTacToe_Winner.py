'''
Tic Tac Toe game
@author: MUHAMMED IRFAN
irfannagath@gmail.com

when prompted , enter your choice as 11 for row 1 col 1
                                     31 for row 3 col 1 etc
                                      Indexing starts at 1
'''
import TicTacToe_Module as ttt
import numpy as np

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in board:
    print i

np_board = np.array(board)
flag = 1
won = False
while True and not(won):
    turn = flag%2
    if turn == 0:
        turn = 2
    print('\nPlayer' + str(turn) + "'s " + " turn")
    myPos = raw_input('')
    NewBoard = ttt.gamer(myPos,np_board,turn)
    won = ttt.solver(NewBoard)
    flag+=1
    if flag == 10:
        print ('\nIt is a Draw!!!')
        print "Thanks for playing!!"
        break


