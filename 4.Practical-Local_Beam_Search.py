import itertools
import random


def tour_cost(tour, dist_matrix):
    """Calculates the total distance of a tour returning to the start city."""
    cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    cost += dist_matrix[tour[-1]][tour[0]]  # Return to origin
    return cost


def get_neighbors(tour):
    """Generates neighbors by swapping every pair of cities (2-opt style swap)."""
    neighbors = []
    n = len(tour)
    for i in range(n):
        for j in range(i + 1, n):
            neighbor = tour.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors


def local_beam_search(dist_matrix, k=3, max_iterations=100):
    """Local Beam Search algorithm for TSP.

    :param dist_matrix: 2D square matrix of distances between cities
    :param k: Beam width (number of states tracked simultaneously)
    :param max_iterations: Maximum steps before termination
    """
    num_cities = len(dist_matrix)
    base_cities = list(range(num_cities))

    # Initialize k random states (tours)
    current_beams = []
    for _ in range(k):
        tour = base_cities.copy()
        random.shuffle(tour)
        current_beams.append(tour)

    best_tour = min(current_beams, key=lambda t: tour_cost(t, dist_matrix))
    best_cost = tour_cost(best_tour, dist_matrix)

    for step in range(max_iterations):
        all_neighbors = []

        # Generate neighbors from all k beams
        for tour in current_beams:
            all_neighbors.extend(get_neighbors(tour))

        # Sort all candidate neighbors by cost
        all_neighbors.sort(key=lambda t: tour_cost(t, dist_matrix))

        # Select the top k best unique neighbors
        unique_beams = []
        for cand in all_neighbors:
            if cand not in unique_beams:
                unique_beams.append(cand)
            if len(unique_beams) == k:
                break

        current_beams = unique_beams
        step_best = current_beams[0]
        step_cost = tour_cost(step_best, dist_matrix)

        # Update the best global solution found
        if step_cost < best_cost:
            best_cost = step_cost
            best_tour = step_best
        else:
            # Reached a local minimum where neighbors cannot improve
            break

    return best_tour, best_cost


# --- Example Usage ---
if __name__ == "__main__":
    # Distance matrix for 5 cities (0 to 4)
    distances = [
        [0, 10, 15, 20, 25],
        [10, 0, 35, 25, 30],
        [15, 35, 0, 30, 20],
        [20, 25, 30, 0, 15],
        [25, 30, 20, 15, 0],
    ]

    # Run Local Beam Search with beam width k=3
    best_route, total_distance = local_beam_search(
        distances, k=3, max_iterations=50
    )

    print(f"Optimal / Best Tour Found: {' -> '.join(map(str, best_route))} -> {best_route[0]}")
    print(f"Total Tour Cost: {total_distance}")