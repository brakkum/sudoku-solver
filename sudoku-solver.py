from sudoku import Sudoku


if __name__ == "__main__":
    """
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        ######################################################
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        ######################################################
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None]
    """
    board = [
        [None,    8, None,    3, None, None, None, None,    7],
        [None, None,    2, None,    1, None, None, None,    6],
        [   7, None,    3,    6,    5, None, None, None, None],
        ######################################################
        [None, None, None, None, None,    8, None,    2, None],
        [   4, None,    8, None, None, None,    7, None,    1],
        [None,    2, None,    1, None, None, None, None, None],
        ######################################################
        [None, None, None, None,    8,    2,    6, None,    4],
        [   8, None, None, None,    4, None,    5, None, None],
        [   2, None, None, None, None,    6, None,    9, None]
    ]
    sudoku = Sudoku(board)
    sudoku.populate_initial_board()
    sudoku.solve_board()





