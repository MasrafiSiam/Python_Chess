from board import Board
from moves import get_king_moves

def main():
    board = Board()
    board.print_board()

    print("\nTesting king at e1 (should be blocked):")
    moves = get_king_moves(board, 7, 4)
    for move in moves:
        print(move)

if __name__ == "__main__":
    main()