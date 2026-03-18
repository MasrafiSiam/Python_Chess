# main.py

from board import Board


def main():
    board = Board()

    print("Initial Board:")
    board.print_board()

    print("\nSwitching turn...")
    board.switch_turn()
    board.print_board()

    print("\nSwitching turn again...")
    board.switch_turn()
    board.print_board()


if __name__ == "__main__":
    main()
