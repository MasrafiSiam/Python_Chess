# moves.py


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
