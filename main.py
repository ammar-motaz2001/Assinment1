import numpy as np

# Function to calculate the attractiveness based on distance
def attractiveness(distance, beta):
    return np.exp(-beta * distance)

# Function to calculate the Euclidean distance between two points
def distance(point1, point2):
    return np.linalg.norm(point1 - point2)

# Function to initialize fireflies randomly
def initialize_fireflies(num_fireflies, num_dimensions):
    return np.random.rand(num_fireflies, num_dimensions)

# Function to evaluate the objective function for a firefly
def evaluate_firefly(firefly):
    # Define your objective function here
    # Example: TSP tour length
    return np.sum(firefly)

# Function to perform the Firefly Algorithm
def firefly_algorithm(num_fireflies, num_dimensions, max_generations, alpha, beta, gamma):
    fireflies = initialize_fireflies(num_fireflies, num_dimensions)
    intensities = np.zeros(num_fireflies)

    for generation in range(max_generations):
        for i in range(num_fireflies):
            for j in range(num_fireflies):
                if evaluate_firefly(fireflies[j]) > evaluate_firefly(fireflies[i]):
                    distance_ij = distance(fireflies[i], fireflies[j])
                    attractiveness_ij = attractiveness(distance_ij, beta)
                    fireflies[i] += alpha * attractiveness_ij * (fireflies[j] - fireflies[i])

        # Update intensities
        for i in range(num_fireflies):
            intensities[i] = evaluate_firefly(fireflies[i])

        # Sort fireflies based on intensities
        sorted_indices = np.argsort(intensities)
        fireflies = fireflies[sorted_indices]

        # Randomize the position of the gamma worst fireflies
        num_randomize = int(gamma * num_fireflies)
        fireflies[-num_randomize:] = initialize_fireflies(num_randomize, num_dimensions)

    # Return the best firefly (solution)
    return fireflies[0]

# Example usage
num_fireflies = 50
num_dimensions = 10
max_generations = 100
alpha = 0.5
beta = 1.0
gamma = 0.1

best_firefly = firefly_algorithm(num_fireflies, num_dimensions, max_generations, alpha, beta, gamma)
print("Best firefly:", best_firefly)
print("Objective value:", evaluate_firefly(best_firefly))


