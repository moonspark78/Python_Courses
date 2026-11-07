def solve_sudoku(board):
    FULL = (1 << 9) - 1
    rows, cols, boxes = [0]*9, [0]*9, [0]*9
    
    for r in range(9):
        for c in range(9):
            v = board[r][c]