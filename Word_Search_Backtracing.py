#!/usr/bin/env python
# coding: utf-8

# In[1]:


def exist(board,word):
    pos = premier_letter_exist(board,word[0])
    if len(word)<=1:
        return pos!=[]
    if pos==[]:
        return False
    cur = ""
    choice = pos
    res = False
    index = 0
    for x in choice:
        i = x[0]
        j = x[1]
        if backtracing(i,j,index,board,word):
            res = True
            break        
    return res

def premier_letter_exist(board,premier):
    pos = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==premier:
                pos.append([i,j])
    return pos
    
def backtracing(i,j,index,board,word):
    if index==len(word):
        return True
    if i>=len(board) or i<0 or j>=len(board[0]) or j<0:
        return False
    else:
        if board[i][j]!=word[index]:
            return False
    tmp = board[i][j]
    board[i][j]="*"
    res = backtracing(i+1,j,index+1,board,word) or backtracing(i-1,j,index+1,board,word) or backtracing(i,j+1,index+1,board,word) or backtracing(i,j-1,index+1,board,word)
    board[i][j]=tmp
    return res
    
        
    
    
board = [
    ["F","Y","C","E","N","R","D"],
    ["K","L","N","F","I","N","U"],
    ["A","A","A","R","A","H","R"],
    ["N","D","K","L","P","N","E"],
    ["A","L","A","N","S","A","P"],
    ["O","O","G","O","T","P","N"],
    ["H","P","O","L","A","N","O"]
]
exist(board,"POLAND")

