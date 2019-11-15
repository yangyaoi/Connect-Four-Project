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
        while (self.board[self.pointer])[rowIndex] == self.em:
            rowIndex++
        if rowIndex < self.dim_col:
            (self.board[self.pointer])[rowIndex] = whos_turn
            self.turn = other_player()
            self.pointer = 0
        return

    def can_drop(self) -> bool:
        """
        checks if the current player can drop a piece in
        the current pointer area
        """
        if valid_move(self.pointer, 0):
            drop()
            return True
        return False

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

    def check_for_win(self, row: int, col: int) -> bool:
        """
        check for a player's win at a certain position
        """
        for dy in {-1, 0, 1}:
            for dx in {-1, 0, 1}:
                if alternation(col, row, dx, dy):
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
<<<<<<< HEAD
            for i in range(4):
                if valid_move(x, y):
                    if self.board[x][y] == self.turn:
                        count++
                        x += dx
                        y += dy
=======
            while count != 4 and valid_move(x, y):
                if self.board[x][y] == self.turn:
                    count += 1
                    x += dx
                    y += dy
>>>>>>> edd2780cb2e508acc158a7c893a777abf77102a3
            return count == 4

    def valid_move(self, col: int, row: int) -> bool:
        """
        Check if the player’s requested drop position is in
        accordance to the game rules and fits in the nested list grid.
        """
        return 0 <= row and row < self.dim_row and 0 <= col and col < self.dim_col
<<<<<<< HEAD

    def is_game_over(self) -> bool:
        """
        check's if the board is filled.
        """
        count = 0
        for x in self.board:
            for y in self.board[x]:
                if self.board[x][y] != self.em:
                    count++
        return count == self.dim_row*self.dim_col
            
                
=======
>>>>>>> edd2780cb2e508acc158a7c893a777abf77102a3
