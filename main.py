from board import Board
from moves import get_rook_moves

def main():
    board = Board()
    board.print_board()

    print("\nTesting rook at a1 (should be blocked):")
    moves = get_rook_moves(board, 7, 0)
    for move in moves:
        print(move)

if __name__ == "__main__":
    main()