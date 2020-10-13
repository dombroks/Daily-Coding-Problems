# -*- coding: utf-8 -*-
"""
This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.
"""

N = 4
#NxN matrix with all elements 0
board = [[0]*N for _ in range(N)]

def is_under_attack(i, j):
    #checking if there is a queen in row or column
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    #checking diagonals
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False

def setting_up_queens_on_board(n):
    #if n is 0, solution found
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (not(is_under_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                #wether we can put the next queen with this arrangment or not
                if setting_up_queens_on_board(n-1)==True:
                    return True
                board[i][j] = 0

    return False
#--------
setting_up_queens_on_board(N)
print("Queens coordinates are: ")
for i in range(N):
  for j in range(N):
    if board[i][j] == 1 :
      print(i,j)
