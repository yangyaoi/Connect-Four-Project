

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
        self.em = "  "
        self.turn = self.p1
        self.board = []
        for x in range(self.dim_row):
            temp = []
            for y in range(self.dim_col):
                temp.append(self.em)
            self.board.append(temp)

    def drop(self, col: int) -> bool:
        """
        Player drops the piece. The player’s character is
        placed in the lowest empty spot in that column.
        """
        y = self.get_drop_loc(col)
        if y == -1:
            return False
        self.board[y][col] = self.turn
        return True

    def other_player(self) -> str:
        if self.turn == self.p1:
            return self.p2
        return self.p1

    def whos_turn(self) -> str:
        """
        Returns who is currently making the move.
        """
        return self.turn

    def switch_turn(self)-> None:
        self.turn = self.other_player()

    def check_for_win(self) -> bool:
        """
        Check whether the player wins. Go through the board
        and see if there is a row, column or diagonal of four
        consecutive pieces of the same player.
        """
        for y in range(self.dim_row):
            for x in range(self.dim_col):
                if self.check_win_at_position(x, y):
                    return True
        return False

    def check_win_at_position(self, row: int, col: int) -> bool:
        """
        check for a player's win at a certain position
        """
        for dy in {-1, 0, 1}:
            for dx in {-1, 0, 1}:
                if self.alternation(row, col, dx, dy):
                    return True
        return False

    def alternation(self, x: int, y: int, dx: int, dy: int) -> bool:
        """
        Helper function for check_for_win function
        """
        if dx == 0 and dy == 0:
            return False
        else:
            for i in range(4):
                if self.valid_move(x, y) and self.board[y][x] == self.turn:
                    x += dx
                    y += dy
                else:
                    return False
            return True

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
        for y in range(self.dim_col):
            for x in range(self.dim_row):
                if self.board[y][x] == self.em:
                    return False
        return True

    def get_drop_loc(self, column: int) -> int:
        """
        return the location on the board which player can place a pieaces according to column.
        """
        for y in range(self.dim_row - 1, -1, -1):
            if self.board[y][column] == self.em:
                return y
        return -1

    def __str__(self):
        final = ""
        for row in self.board:
            final += ",".join(row) + "\n"
        return final
