from board import Board
from moves import get_queen_moves

def main():
    board = Board()
    board.print_board()

    print("\nTesting queen at d1 (should be blocked):")
    moves = get_queen_moves(board, 7, 3)
    for move in moves:
        print(move)

if __name__ == "__main__":
    main()