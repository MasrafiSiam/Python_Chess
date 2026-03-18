import copy
from rules import is_in_check


def get_pawn_moves(board, row, col):
    moves = []
    piece = board.board[row][col]

    # White pawn
    if piece == "P":
        # Move forward 1
        if row > 0 and board.board[row - 1][col] == ".":
            moves.append((row, col, row - 1, col))

        # First move (2 steps)
        if (
            row == 6
            and board.board[row - 1][col] == "."
            and board.board[row - 2][col] == "."
        ):
            moves.append((row, col, row - 2, col))

        # Capture left
        if row > 0 and col > 0 and board.board[row - 1][col - 1].islower():
            moves.append((row, col, row - 1, col - 1))

        # Capture right
        if row > 0 and col < 7 and board.board[row - 1][col + 1].islower():
            moves.append((row, col, row - 1, col + 1))

    # Black pawn
    elif piece == "p":
        # Move forward 1
        if row < 7 and board.board[row + 1][col] == ".":
            moves.append((row, col, row + 1, col))

        # First move (2 steps)
        if (
            row == 1
            and board.board[row + 1][col] == "."
            and board.board[row + 2][col] == "."
        ):
            moves.append((row, col, row + 2, col))

        # Capture left
        if row < 7 and col > 0 and board.board[row + 1][col - 1].isupper():
            moves.append((row, col, row + 1, col - 1))

        # Capture right
        if row < 7 and col < 7 and board.board[row + 1][col + 1].isupper():
            moves.append((row, col, row + 1, col + 1))

    return moves


def get_knight_moves(board, row, col):
    moves = []
    piece = board.board[row][col]

    # All possible knight moves
    directions = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1),
    ]

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r <= 7 and 0 <= c <= 7:
            target = board.board[r][c]
            if piece.isupper():
                # White knight: can move to empty or black piece
                if target == "." or target.islower():
                    moves.append((row, col, r, c))
            else:
                # Black knight: can move to empty or white piece
                if target == "." or target.isupper():
                    moves.append((row, col, r, c))

    return moves


def get_bishop_moves(board, row, col):
    moves = []
    piece = board.board[row][col]

    directions = [
        (-1, -1), (-1, 1),
        (1, -1), (1, 1)
    ]

    for dr, dc in directions:
        r, c = row + dr, col + dc

        while 0 <= r <= 7 and 0 <= c <= 7:
            target = board.board[r][c]

            if target == ".":
                moves.append((row, col, r, c))
            else:
                # If enemy piece → capture
                if piece.isupper() and target.islower():
                    moves.append((row, col, r, c))
                elif piece.islower() and target.isupper():
                    moves.append((row, col, r, c))

                # Stop after hitting any piece
                break

            r += dr
            c += dc

    return moves

def get_rook_moves(board, row, col):
    moves = []
    piece = board.board[row][col]

    directions = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1)
    ]

    for dr, dc in directions:
        r, c = row + dr, col + dc

        while 0 <= r <= 7 and 0 <= c <= 7:
            target = board.board[r][c]

            if target == ".":
                moves.append((row, col, r, c))
            else:
                # Capture enemy piece
                if piece.isupper() and target.islower():
                    moves.append((row, col, r, c))
                elif piece.islower() and target.isupper():
                    moves.append((row, col, r, c))

                break  # stop after hitting any piece

            r += dr
            c += dc

    return moves

def get_queen_moves(board, row, col):
    moves = []

    # Queen = bishop + rook
    moves.extend(get_bishop_moves(board, row, col))
    moves.extend(get_rook_moves(board, row, col))

    return moves

def get_king_moves(board, row, col):
    moves = []
    piece = board.board[row][col]

    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    for dr, dc in directions:
        r, c = row + dr, col + dc

        if 0 <= r <= 7 and 0 <= c <= 7:
            target = board.board[r][c]

            if piece.isupper():
                if target == "." or target.islower():
                    moves.append((row, col, r, c))
            else:
                if target == "." or target.isupper():
                    moves.append((row, col, r, c))

    return moves

def get_all_moves(board):
    all_moves = []

    for row in range(8):
        for col in range(8):
            piece = board.board[row][col]

            if piece == ".":
                continue

            # White turn
            if board.turn == "white" and piece.isupper():

                if piece == "P":
                    all_moves.extend(get_pawn_moves(board, row, col))
                elif piece == "N":
                    all_moves.extend(get_knight_moves(board, row, col))
                elif piece == "B":
                    all_moves.extend(get_bishop_moves(board, row, col))
                elif piece == "R":
                    all_moves.extend(get_rook_moves(board, row, col))
                elif piece == "Q":
                    all_moves.extend(get_queen_moves(board, row, col))
                elif piece == "K":
                    all_moves.extend(get_king_moves(board, row, col))

            # Black turn
            elif board.turn == "black" and piece.islower():

                if piece == "p":
                    all_moves.extend(get_pawn_moves(board, row, col))
                elif piece == "n":
                    all_moves.extend(get_knight_moves(board, row, col))
                elif piece == "b":
                    all_moves.extend(get_bishop_moves(board, row, col))
                elif piece == "r":
                    all_moves.extend(get_rook_moves(board, row, col))
                elif piece == "q":
                    all_moves.extend(get_queen_moves(board, row, col))
                elif piece == "k":
                    all_moves.extend(get_king_moves(board, row, col))

    return all_moves

def get_all_legal_moves(board):
    legal_moves = []

    all_moves = get_all_moves(board)

    for move in all_moves:
        # Create a copy of board
        new_board = copy.deepcopy(board)

        # Make the move
        new_board.make_move(move)

        # If king is NOT in check → valid move
        if not is_in_check(new_board, board.turn):
            legal_moves.append(move)

    return legal_moves