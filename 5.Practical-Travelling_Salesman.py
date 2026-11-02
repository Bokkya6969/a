from collections import deque

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)          # 0 = blank

# Moves of the blank: (name, row delta, col delta)
MOVES = [("Up", -1, 0), ("Down", 1, 0), ("Left", 0, -1), ("Right", 0, 1)]

def successors(state):
    """Generate (action, new_state) pairs."""
    idx = state.index(0)
    r, c = divmod(idx, 3)
    for name, dr, dc in MOVES:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            nidx = nr * 3 + nc
            s = list(state)
            s[idx], s[nidx] = s[nidx], s[idx]   # slide tile into blank
            yield name, tuple(s)

def is_solvable(state):
    """8-puzzle is solvable iff the number of inversions is even."""
    tiles = [x for x in state if x != 0]
    inv = sum(1 for i in range(len(tiles))
                for j in range(i + 1, len(tiles))
                if tiles[i] > tiles[j])
    return inv % 2 == 0

def bfs(start, goal=GOAL):
    if not is_solvable(start):
        return None, 0
    queue = deque([(start, [])])
    visited = {start}
    expanded = 0
    while queue:
        state, path = queue.popleft()
        expanded += 1
        if state == goal:
            return path, expanded
        for action, nxt in successors(state):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [action]))
    return None, expanded

def show(state):
    for i in range(0, 9, 3):
        print(" ".join(str(x) if x else "_" for x in state[i:i+3]))
    print()

if __name__ == "__main__":
    start = (1, 2, 3,
             4, 0, 6,
             7, 5, 8)

    plan, expanded = bfs(start)
    if plan is None:
        print("No solution.")
    else:
        print(f"Plan ({len(plan)} moves): {plan}")
        print(f"States expanded: {expanded}\n")
        # replay the plan
        state = start
        show(state)
        for a in plan:
            for name, nxt in successors(state):
                if name == a:
                    state = nxt
                    break
            print("Move blank", a)
            show(state)