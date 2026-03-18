# rules.py

from moves import get_all_moves

def find_king(board, color):
    king = "K" if color == "white" else "k"

    for row in range(8):
        for col in range(8):
            if board.board[row][col] == king:
                return (row, col)

    return None


def is_in_check(board, color):
    king_pos = find_king(board, color)

    if king_pos is None:
        return False

    # Save current turn
    original_turn = board.turn

    # Switch to opponent
    board.turn = "black" if color == "white" else "white"

    opponent_moves = get_all_moves(board)

    # Restore turn
    board.turn = original_turn

    # Check if any move attacks king
    for move in opponent_moves:
        _, _, to_row, to_col = move
        if (to_row, to_col) == king_pos:
            return True

    return False