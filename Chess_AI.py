#!/usr/bin/env python
# coding: utf-8

# In[1]:


import chess
import chess.polyglot
board = chess.Board()
display(board)


# In[2]:


pawn_table=[
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0]
knight_table = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50]
bishop_table = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20]
rook_table = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0]
queen_table = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20]
king_table = [
    20, 30, 40, 0, 0, 10, 40, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30]


# In[3]:


def evaluation():
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0

    pawn_white = len(board.pieces(chess.PAWN, chess.WHITE))
    pawn_black = len(board.pieces(chess.PAWN, chess.BLACK))
    ghoda_white = len(board.pieces(chess.KNIGHT, chess.WHITE))
    ghoda_black = len(board.pieces(chess.KNIGHT, chess.BLACK))
    bishop_white = len(board.pieces(chess.BISHOP, chess.WHITE))
    bishop_black = len(board.pieces(chess.BISHOP, chess.BLACK))
    rook_white = len(board.pieces(chess.ROOK, chess.WHITE))
    rook_black = len(board.pieces(chess.ROOK, chess.BLACK))
    white_queen = len(board.pieces(chess.QUEEN, chess.WHITE))
    black_queen = len(board.pieces(chess.QUEEN, chess.BLACK))

    material = 100 * ( pawn_white - pawn_black) + 320 * (ghoda_white-ghoda_black) + 330 * (bishop_white-bishop_black) + 500 * (rook_white - rook_black) + 900 * (white_queen-black_queen)

    pawndiff_white = sum([pawn_table[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
    pawndiff_black = sum([-pawn_table[chess.square_mirror(i)]for i in board.pieces(chess.PAWN, chess.BLACK)])
    
    knightdiff_white = sum([knight_table[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    knightdiff_black =  sum([-knight_table[chess.square_mirror(i)]for i in board.pieces(chess.KNIGHT, chess.BLACK)])
    
    bishopdiff_white = sum([bishop_table[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
    bishopdiff_black =  sum([-bishop_table[chess.square_mirror(i)] for i in board.pieces(chess.BISHOP, chess.BLACK)])
    
    rookdiff_white = sum([rook_table[i] for i in board.pieces(chess.ROOK, chess.WHITE)])
    rookdiff_black =  sum([-rook_table[chess.square_mirror(i)]for i in board.pieces(chess.ROOK, chess.BLACK)])
    
    queendiff_white = sum([queen_table[i] for i in board.pieces(chess.QUEEN, chess.WHITE)])
    queendiff_black =sum([-queen_table[chess.square_mirror(i)]for i in board.pieces(chess.QUEEN, chess.BLACK)])
    
    kingdiff_white = sum([king_table[i] for i in board.pieces(chess.KING, chess.WHITE)])
    kingdiff_black = sum([-king_table[chess.square_mirror(i)] for i in board.pieces(chess.KING, chess.BLACK)])

    eval = material + (pawndiff_white+pawndiff_black) + (knightdiff_white+knightdiff_black) + (bishopdiff_white+bishopdiff_black) + (rookdiff_white+rookdiff_black) + (queendiff_white+queendiff_black) + (kingdiff_white+kingdiff_black)
    if board.turn:
        return eval
    else:
        return -eval


# In[4]:


def selectmove(depth):
    try:
        move = chess.polyglot.MemoryMappedReader("C:/Users/praty/Downloads/human.bin").weighted_choice(board).move
        return move
    except:
        bestmove=chess.Move.null()
        bestvalue=-99999
        alpha=-100000
        beta=100000
        for move in board.legal_moves:
            board.push(move)
            boardvalue= -alphabeta(-beta,-alpha,depth-1)
            if boardvalue>bestvalue:
                bestvalue=boardvalue
                bestmove=move
            if boardvalue>alpha:
                alpha = boardvalue
            board.pop()
        return bestmove
    


# In[5]:


def alphabeta(alpha,beta,depth):
    bestscore=-9999
    if(depth==0):
        return quiescence(alpha,beta)
    for move in board.legal_moves:
        board.push(move)
        score=-alphabeta(-beta,-alpha,depth-1)
        board.pop()
        if(score>=beta):
            return score
        if(score>bestscore):
            bestscore=score
        if(score>alpha):
            alpha=score
    return bestscore


# In[6]:


def quiescence(alpha,beta,a=5):
    evaluate=evaluation()
    
    if(evaluate>=beta):
        return beta 
    if(alpha<evaluate):
        alpha=evaluate
    for move in board.legal_moves:
        if(a>0):
            if board.is_capture(move):
                board.push(move)
                score=-quiescence(-beta,-alpha,a-1)
                board.pop()
                if(score>=beta):
                    return beta 
                if(score>alpha):
                    alpha=score
        else:
            return alpha 
    return alpha
            
        


# In[8]:


while not board.is_game_over(claim_draw=True):
    if(board.turn==False):
        move=str(input())
        print("\n")
        board.push_san(move)
        display(board)
    else:
        depth=3
        move=selectmove(depth)
        board.push(move)
        display(board)


# In[15]:





# In[ ]:





# In[ ]:




