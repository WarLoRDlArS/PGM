import numpy as np

# Function to get a matrix input from the user
def get_matrix(rows, cols, name="matrix"):
    matrix = []
    print(f"Enter the values for {name} ({rows}x{cols}):")
    for i in range(rows):
        row = input(f"Row {i + 1} (separate values with spaces): ").strip().split()
        matrix.append([float(x) for x in row])
    return np.array(matrix)

# Function to get a vector input from the user
def get_vector(length, name="vector"):
    vector = input(f"Enter the values for {name} (separate values with spaces): ").strip().split()
    return np.array([float(x) for x in vector])

# Get user input for the transition matrix P and initial state vector Q
P = get_matrix(3, 3, "transition matrix P")
Q = get_vector(3, "initial state vector Q")

# Get the number of days for prediction
days = int(input("Enter the number of days for weather prediction: "))

# 1. Weather prediction for the specified number of days
predicted_weather = [Q]
current_state = Q
for _ in range(days):
    current_state = np.dot(current_state, P)
    predicted_weather.append(current_state)

predicted_weather = np.array(predicted_weather)

print("\nWeather prediction for the specified number of days:")
for i, day in enumerate(predicted_weather):
    print(f"Day {i}: Sunny = {day[0]:.4f}, Cloudy = {day[1]:.4f}, Rainy = {day[2]:.4f}")

# 2. Probability of transitioning from Sunny to Rainy in three days
P_3 = np.linalg.matrix_power(P, 3)
sunny_to_rainy_3_days = P_3[0, 2]

print(f"\nProbability of transitioning from Sunny to Rainy in 3 days: {sunny_to_rainy_3_days:.4f}")

# 3. Overall probability of all weather states after five days
P_5 = np.linalg.matrix_power(P, 5)
probability_after_5_days = np.dot(Q, P_5)

print(f"\nOverall probabilities after 5 days: Sunny = {probability_after_5_days[0]:.4f}, "
      f"Cloudy = {probability_after_5_days[1]:.4f}, Rainy = {probability_after_5_days[2]:.4f}")