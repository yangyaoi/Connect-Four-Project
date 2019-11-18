

class ConnectFourBoard:

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

    def move_left(self) -> None:
        """
        Player moves drop spot one column to the left.
        """
        n = self.pointer-1
        if self.valid_move(n, 0):
            self.pointer -= 1

    def move_right(self) -> None:
        """
        Player moves drop spot one column to the right.
        """
        n = self.pointer+1
        if self.valid_move(n, 0):
            self.pointer += 1

    def drop(self, col: int) -> None:
        """
        Player drops the piece. The player’s character is
        placed in the lowest empty spot in that column.
        """
        self.pointer = col-1
        row_index = 0
        for x in range(self.dim_row):
            if self.board[self.pointer][row_index] == self.em:
                row_index += 1
            else:
                break
        self.board[self.pointer][row_index-1] = self.turn
        self.turn = self.other_player()
        self.pointer = 0

    def can_drop(self, col: int) -> bool:
        """
        checks if the current player can drop a piece in
        the current pointer area
        """
        return self.valid_move(col, 0)

    def other_player(self) -> str:
        if self.turn == self.p1:
            return self.p2
        return self.p1

    def whos_turn(self) -> str:
        """
        Returns who is currently making the move.
        """
        return self.turn

    def swith_turn(self)-> None:
        if self.turn == self.p1:
            self.turn = self.p2
        else:
            self.turn = self.p1


    def check_for_win(self) -> bool:
        """
        Check whether the player wins. Go through the board
        and see if there is a row, column or diagonal of four
        consecutive pieces of the same player.
        """
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                for dy in {-1, 0, 1}:
                    for dx in {-1, 0, 1}:
                        if self.alternation(x, y, dx, dy):
                            return True
                        pass
        return False

    def check_win_at_position(self, row: int, col: int) -> bool:
        """
        check for a player's win at a certain position
        """
        for dy in {-1, 0, 1}:
            for dx in {-1, 0, 1}:
                if self.alternation(col, row, dx, dy):
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
            for i in range(4):
                if self.valid_move(x, y):
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
        return 0 <= row < self.dim_row and 0 <= col < self.dim_col

    def is_game_over(self) -> bool:
        """
        check's if the board is filled.
        """
        count = 0
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] != self.em:
                    count += 1
        return count == self.dim_row*self.dim_col
    def get_drop_loc(self,column:int) -> int:
        """
        return the location on the board which player can place a pieaces according to column.
        """
        if self.can_drop(column):
            if self.board[column][5] == self.em:
                return 5
            row_index = 0
            for x in range(self.dim_row):
                if self.board[column][row_index] == self.em:
                    row_index += 1
                else:
                    break
            return row_index
