from queue import PriorityQueue

def a_star(graph, start, goal, heuristic):
    pq = PriorityQueue()
    pq.put((0, start))  

    g_cost = {start: 0}
    parent = {start: None}

    while not pq.empty():
        current = pq.get()[1]

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1], g_cost[goal]

        for neighbor, cost in graph[current]:
            new_cost = g_cost[current] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]
                pq.put((f_cost, neighbor))
                parent[neighbor] = current

    return None, float("inf")


# Graph representation
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 4)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values (estimated cost to goal G)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 1,
    'G': 0
}

start = 'A'
goal = 'G'

path, cost = a_star(graph, start, goal, heuristic)

print("Shortest Path:", " -> ".join(path))
print("Total Cost:", cost)