def solve_sudoku(board):
    FULL = (1 << 9) - 1
    rows, cols, boxes = [0]*9, [0]*9, [0]*9
    
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v:
                bit = 1 << (v - 1)
                b = (r // 3) * 3 + c // 3
                if rows[r] & bit or cols[c] & bit or boxes[b] & bit:
                    return False
                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit
                
    def backtrack():
        best, candidates = None, None
        min_count = 10
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    b = (r // 3) * 3 + c // 3
                    mask = FULL & ~(rows[r] | cols[c] | boxes[b])
                    count = mask.bit_count()
                    if count == 0:
                        return False
                    if count < min_count:
                        best, candidates = (r, c, b), mask
                        min_count = count
                        

        if best is None:
            return True
        r, c, b = best
        while candidates:
            bit = candidates & -candidates
            candidates ^= bit
            value = bit.bit_length
            board[r][c] = value
            rows[r] |= bit
            cols[c] |= bit