from sudoku import Sudoku


if __name__ == "__main__":
    """
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None]
    """
    board = [
        [None, None,    8,    2,    5, None,    7, None,    1],
        [None,    2, None, None, None,    4,    8, None, None],
        [None, None,    4, None, None,    6, None, None, None],
        [None,    7, None,    4, None,    8, None,    3,    5],
        [None,    4,    5, None,    9, None,    2,    7, None],
        [   6,    1, None,    5, None,    2, None,    8, None],
        [None, None, None,    6, None, None,    3, None, None],
        [None, None,    7,    9, None, None, None,    1, None],
        [   1, None,    6, None,    2,    5,    4, None, None]
    ]
    sudoku = Sudoku(board)
    sudoku.populate_initial_board()





