from board import Board
from moves import get_pawn_moves, get_knight_moves

def main():
    board = Board()
    board.print_board()

    print("\nWhite pawn e2 moves:")
    pawn_moves = get_pawn_moves(board, 6, 4)
    for move in pawn_moves:
        print(move)

    print("\nWhite knight g1 moves:")
    knight_moves = get_knight_moves(board, 7, 6)
    for move in knight_moves:
        print(move)

if __name__ == "__main__":
    main()