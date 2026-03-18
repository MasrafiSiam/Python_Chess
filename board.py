class Board:
    def __init__(self):
        self.board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ]
        self.turn = "white"

    def print_board(self):
        print("  a b c d e f g h")
        for i in range(8):
            print(8 - i, end=" ")
            for j in range(8):
                print(self.board[i][j], end=" ")
            print()
        print(f"Turn: {self.turn}")

    def switch_turn(self):
        self.turn = "black" if self.turn == "white" else "white"

    def make_move(self, move):
        from_row, from_col, to_row, to_col = move

        piece = self.board[from_row][from_col]

        # Move piece
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = "."

        # Switch turn
        self.switch_turn()