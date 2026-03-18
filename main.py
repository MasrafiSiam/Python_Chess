from board import Board
from rules import is_in_check

def main():
    board = Board()

    # Create a check situation manually
    board.board[6][4] = "."   # remove white pawn (e2)
    board.board[1][4] = "."   # remove black pawn (e7)
    board.board[3][4] = "q"   # put black queen at e5

    board.print_board()

    print("\nIs white in check?")
    print(is_in_check(board, "white"))

if __name__ == "__main__":
    main()