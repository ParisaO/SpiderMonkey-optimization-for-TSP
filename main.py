import time
import numpy as np
import random
from Spider_Monkey import Spider_Monkey

start = time.time()
file_path = '1000_randomDistance.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()
    num_cities = int(lines[0].strip())  # The first line contains the number of cities
    distances = [[0]*num_cities for _ in range(num_cities)]  # Initialize a matrix with zeros

    # Process each line after the first two lines
    for line in lines[2:]:
        node1, node2, distance = line.split()
        i, j = int(node1)-1, int(node2)-1  # Convert to 0-based index
        distances[i][j] = distances[j][i] = float(distance)  # Fill both entries due to symmetry

# Convert the list of lists into a numpy array for better handling
distance_matrix = np.array(distances)
Itr = 10000
LLL = 3
GLL = 3
pr = 0.1
N = 200
MG = 4
N_states = 1000
plot = True
args = [Itr, MG, LLL, GLL, pr, N, N_states, distance_matrix, plot]
Spider_Monkey(*args)
end = time.time()
print('Time: ', end - start)
