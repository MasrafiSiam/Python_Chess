from board import Board
from moves import get_bishop_moves

def main():
    board = Board()
    board.print_board()

    print("\nTesting bishop at c1 (should be blocked):")
    moves = get_bishop_moves(board, 7, 2)
    for move in moves:
        print(move)

if __name__ == "__main__":
    main()