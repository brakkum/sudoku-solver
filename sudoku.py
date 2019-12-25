from termcolor import cprint


class Sudoku:
    """
    a 2D array that represents a sudoku board
    :param initial_board:
    """
    def __init__(self, initial_board):
        self.is_solved = False
        self.iterations = 0
        # the game board used after the initial_board is parsed.
        # an array that has 9 arrays that have 9 values each
        # self.board[0] is the first row
        # self.board[0][0] - self.board[0][8] is the first column
        self.board = [[None for _ in range(9)] for _ in range(9)]
        # possible values for each individual cell
        self.possible_cell_nums = [[[_ for _ in range(1, 10)] for _ in range(9)] for _ in range(9)]
        self.initial_board = initial_board

    def populate_initial_board(self):
        cprint("Populate initial board", "green")
        # iterate over the initial board by row
        for i, row in enumerate(self.initial_board):
            # iterate over each cell in the row
            for j, cell in enumerate(row):
                # if a cell has a value, update the board and possible nums
                if cell is not None:
                    self.board[i][j] = cell
                    self.possible_cell_nums[i][j] = [cell]

    def solve_board(self):
        while not self.is_solved:
            self.update_rows()
            self.update_columns()
            self.update_squares()
            self.iterations += 1
            self.check_board()
            cprint("{} iterations".format(self.iterations), "magenta")

    def update_rows(self):
        cprint("Update rows", "green")
        # iterate over current rows in board
        for i in range(len(self.board)):
            cprint("Row {}".format(i), "cyan")
            row = self.board[i]
            # what numbers are already populated for this row
            existing_row_nums = [_ for _ in row if _ is not None]
            print("Existent row nums: {}".format(existing_row_nums))
            # iterate over each cell in the row
            for j in range(len(row)):
                print("cell {} of row {}: {}".format(j, i, self.board[i][j]))
                # the possible values known so far for the current cell
                cell_possible_nums = self.possible_cell_nums[i][j]
                # if the length of cell possible nums is already one, then we're done here
                if len(cell_possible_nums) == 1:
                    continue
                # update the possible nums based on what nums are already in the row
                new_possible_cell_nums = [num for num in cell_possible_nums if num not in existing_row_nums]
                # set it and forget it
                self.possible_cell_nums[i][j] = new_possible_cell_nums
                print("cell possible nums: {}".format(cell_possible_nums))
                # if the length of new possible cell nums is 1, we just found the number
                if len(new_possible_cell_nums) == 1:
                    if self.board[i][j] is None:
                        print("updating board[{}][{}]: {}".format(i, j, new_possible_cell_nums[0]))
                        self.board[i][j] = new_possible_cell_nums[0]

    def update_columns(self):
        cprint("Update columns", "green")
        # iterate over current rows in board
        for i in range(len(self.board)):
            col = [_ for _ in [row[i] for row in self.board]]
            cprint("column {}: {}".format(i, col), "cyan")
            # what numbers are already populated for this column
            existing_col_nums = [ _ for _ in col if _ is not None ]
            print("Existent col nums: {}".format(existing_col_nums))
            # iterate over each cell in the column
            for j in range(len(col)):
                print("cell {} of col {}: {}".format(j, i, self.board[j][i]))
                # the possible values known so far for the current cell
                cell_possible_nums = self.possible_cell_nums[j][i]
                # if it's already one long, we already have the num
                if len(cell_possible_nums) == 1:
                    continue
                # update the possible nums based on what nums are already in the row
                new_possible_cell_nums = [num for num in cell_possible_nums if num not in existing_col_nums]
                # set it and forget it
                self.possible_cell_nums[j][i] = new_possible_cell_nums
                print("cell possible nums: {}".format(cell_possible_nums))
                # if the length of possible cell nums is 1, that's the answer
                if len(new_possible_cell_nums) == 1:
                    if self.board[j][i] is None:
                        print("updating board[{}][{}]: {}".format(j, i, new_possible_cell_nums[0]))
                        self.board[j][i] = new_possible_cell_nums[0]
        [print(_) for _ in self.possible_cell_nums]

    def update_squares(self):
        # loop over number of squares on x
        for i in range(3):
            # loop over number of squares on y
            for j in range(3):
                pass

    def check_board(self):
        pass
