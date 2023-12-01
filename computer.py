# computer.py
# minimax algorithm for AI to play checkers. Written by https://github.com/techwithtim and modified by us.
# code from reference repo: https://github.com/techwithtim/Python-Checkers-AI

from copy import deepcopy
import pygame
from constants import RED, WHITE

pygame.init()
pygame.mixer.init()


def minimax(position, depth, max_player, game): # minimax algorithm for AI to play checkers
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
        #prints computer thinking until made a move
        move_sound = pygame.mixer.Sound('music/sliding.mp3')
        move_sound.set_volume(0.4)
        if not pygame.mixer.get_busy():
            move_sound.play()
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move

def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

def get_all_moves(board, color, game): # get all possible moves for a given color
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # draw_moves(game, board, piece) # uncommenting this will show all possible AI moves
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves

def draw_moves(game, board, piece): # draw all possible moves for a given piece
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    #pygame.time.delay(100)
