from board import Board
from moves import get_all_moves

def main():
    board = Board()
    board.print_board()

    print("\nAll possible moves for white:")
    moves = get_all_moves(board)

    for move in moves:
        print(move)

    print(f"\nTotal moves: {len(moves)}")

if __name__ == "__main__":
    main()