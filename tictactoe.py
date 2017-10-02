"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(120)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    if board.check_win():
        return SCORES[board.check_win()],(-1,-1)
    
        
    multiplier = SCORES[player]
    
    best_move = (-2*multiplier, (-1,-1))
        
    for empty_square in board.get_empty_squares():
        board1 = board.clone()
        board1.move(empty_square[0],empty_square[1],player)
        
        #print board1
        
        child_mm_move = mm_move(board1,provided.switch_player(player))
        
        if child_mm_move[0]*multiplier == 1:
            return child_mm_move[0],empty_square
        
        if child_mm_move[0]*multiplier > best_move[0]*multiplier:
            best_move = (child_mm_move[0],empty_square)
    
    #print best_move
    return best_move
            
        
def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(move_wrapper, 1, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
