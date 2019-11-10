from typing import TextIO, List, Dict, Tuple

class ConnectFourBoard():

    def __init__(self, rows: int, cols: int) -> None:
        """
        Get the length and width of the board and create the grid using the length and width dimentions.
        """
        self.dim_row = rows
        self.dim_col = cols
        self.pointer = 0
        self.p1 = "P1"
        self.p2 = "P2"
        self.em = "EMPTY"
        self.bo = "BOTH"
        self.turn = self.p1
        self.board = []
        for x in range(self.dim_col):
            temp = []
            for y in range(self.dim_row):
                temp.append(self.em)
            self.board.append(temp)
        return

    def move_left(self) -> None:
        """
        Player moves drop spot one column to the left.
        """
        n = self.pointer-1
        if valid_move(n, 0):
            self.pointer -= 1
        return

    def move_right(self) -> None:
        """
        Player moves drop spot one column to the right.
        """
        n = self.p1_pointer+1
        if valid_move(n, 0):
            self.p1_pointer += 1
        return

    def drop(self) -> None:
        """
        Player drops the piece. The player’s character is
        placed in the lowest empty spot in that column.
        """
        rowIndex = 0
        if valid_move(self.pointer, 0):
            while (self.board[self.pointer])[rowIndex] == self.em:
                rowIndex += 1
            if rowIndex < self.dim_col:
                (self.board[self.pointer])[rowIndex] = whos_turn
                whos_turn = other_player()
                self.pointer = 0
        else:
            return "cannot drop there"

    def other_player(self) -> str:
        if self.turn == self.p1:
            return self.p2
        return self.p1

    def whos_turn(self) -> str:
        """
        Returns who is currently making the move.
        """
        return self.turn

    def check_for_win(self) -> bool:
        """
        Check whether the player wins. Go through the board
        and see if there is a row, column or diagonal of four
        consecutive pieces of the same player.
        """
        for x in self.board:
            for y in self.board[x]:
                for dy in {-1, 0, 1}:
                    for dx in {-1, 0, 1}:
                        if alternation(x, y, dx, dy):
                            return True
                        pass
        return False

    def alternation(self, x: int, y: int, dx: int, dy: int) -> bool:
        """
        Helper function for check_for_win function
        """
        count = 0
        if dx == 0 and dy == 0:
            return False
        else:
            while count != 4 and valid_move(x, y):
                if self.board[x][y] == self.turn:
                    count += 1
                    x += dx
                    y += dy
            return count == 4

    def valid_move(self, col: int, row: int) -> bool:
        """
        Check if the player’s requested drop position is in
        accordance to the game rules and fits in the nested list grid.
        """
        return 0 <= row and row < self.dim_row and 0 <= col and col < self.dim_col
