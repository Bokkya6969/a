N = 8

def is_consistent(cols, row, col):
    """Check the new queen (row, col) against queens already placed in rows 0..row-1."""
    for r in range(row):
        c = cols[r]
        if c == col or abs(c - col) == row - r:    
            return False
    return True

def backtrack(cols, row=0, stats=None):
    if stats is not None:
        stats["nodes"] += 1
    if row == N:
        return cols[:]                  
    for col in range(N):
        if is_consistent(cols, row, col):
            cols.append(col)            
            result = backtrack(cols, row + 1, stats)
            if result is not None:
                return result
            cols.pop()                  
    return None


def backtrack_all(cols, row=0, solutions=None):
    if solutions is None:
        solutions = []
    if row == N:
        solutions.append(cols[:])
        return solutions
    for col in range(N):
        if is_consistent(cols, row, col):
            cols.append(col)
            backtrack_all(cols, row + 1, solutions)
            cols.pop()
    return solutions

def show(cols):
    for c in cols:
        print(" ".join("Q" if j == c else "." for j in range(N)))
    print()

if __name__ == "__main__":
    stats = {"nodes": 0}
    sol = backtrack([], 0, stats)
    print("First solution (column of queen in each row):", sol)
    print("Search nodes visited:", stats["nodes"], "\n")
    show(sol)

    all_sols = backtrack_all([])
    print("Total solutions:", len(all_sols))