def solve_sudoku(board):
    FULL = (1 << 9) - 1
    rows, cols, boxes = [0]*9, [0]*9, [0]*9