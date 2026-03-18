# main.py

from board import Board
from moves import get_pawn_moves

def main():
    board = Board()
    board.print_board()

    print("\nTesting pawn moves for white pawn at e2:")

    # e2 → row 6, col 4
    moves = get_pawn_moves(board, 6, 4)

    for move in moves:
        print(move)


if __name__ == "__main__":
    main()