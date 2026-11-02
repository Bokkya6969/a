# Capacities of the two jugs and target amount
CAP_A = 4
CAP_B = 3
TARGET = 2


def get_next_states(state):
    """Generates all 6 possible valid transitions from (a, b)."""
    a, b = state
    transitions = []
 
    transitions.append((CAP_A, b))

    transitions.append((a, CAP_B))
 
    transitions.append((0, b))
 
    transitions.append((a, 0))
 
    pour_a_to_b = min(a, CAP_B - b)
    transitions.append((a - pour_a_to_b, b + pour_a_to_b))
 
    pour_b_to_a = min(b, CAP_A - a)
    transitions.append((a + pour_b_to_a, b - pour_b_to_a))

    return transitions

def dfs_solve(cap_a, cap_b, target):
    """Solves the problem using an explicit LIFO stack (DFS)."""
    start_state = (0, 0)
    stack = [(start_state, [start_state])]
    visited = set()

    while stack:
        current_state, path = stack.pop()   

        a, b = current_state
 
        if a == target:
            return path

        if current_state in visited:
            continue
        visited.add(current_state)
 
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                stack.append((next_state, path + [next_state]))

    return None

solution_path = dfs_solve(CAP_A, CAP_B, TARGET)

if solution_path:
    print(f"Goal reached in {len(solution_path) - 1} steps:\n")
    for step, (j1, j2) in enumerate(solution_path):
        print(f"Step {step}: Jug A = {j1}L, Jug B = {j2}L")
else:
    print("No solution possible.")