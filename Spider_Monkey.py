import numpy as np
import random
import matplotlib.pyplot as plt
from SS_function import cost_calculator


def Spider_Monkey(Itr, MG, LLL, GLL, pr, N, N_states, distance_matrix, plot=False):
    """
    :param Itr: Total number of iterations
    :param MG: Allowed maximum groups
    :param LLL: Local Leader Limit
    :param GLL: Global Leader Limit
    :param pr: Perturbation rate
    :param N: Total number of Spider Monkeys
    :param N_states: Total number of cities
    :param distance_matrix : cost of each path
    :param plot: binary indicator of plotting the results
    :return: The best solution
    """
    monkeys = [random.randint(1, N_states) for _ in range(N)]

    # Create N random routes
    array = list(range(2, N_states + 1))
    random.shuffle(array)
    distinct_arrays = [random.sample(array, len(array)) for _ in range(N)]
    modified_arrays = [[1] + row + [1] for row in distinct_arrays]

    cost = []
    cost_min_plot = []

    for i in range(N):
        cost.append(cost_calculator(modified_arrays[i], distance_matrix))
    cost_min_plot.append(min(cost))

    print("Initial cost for each monkey:", [f"{c:.3f}" for c in cost])
    global_leader = cost.index(min(cost)) + 1
    print("Global Leader:", global_leader)

    for i in range(Itr):

        c = [random.sample(array, len(array)) for _ in range(N)]
        modified_c = [[1] + row + [1] for row in c]

        cost2 = []
        for j in range(N):
            cost2.append(cost_calculator(modified_c[j], distance_matrix))

            if cost2[j] < cost[j]:  # Updating the route and cost if progressed is seen
                modified_arrays[j] = modified_c[j]
                cost[j] = cost2[j]

        cost_min_plot.append(min(cost))
        print("Minimum cost:", min(cost))

    if plot:
        plt.figure(dpi=200)
        plt.plot(np.array(cost_min_plot), 'b', label="Minimum Cost", linewidth=2)
        plt.xlabel(r"$iteration$")
        plt.ylabel(r"$cost")
        plt.title("randomDistance cities")
        plt.legend()
        plt.grid()
        plt.show()

    GL = cost.index(min(cost)) + 1
    print("Final Mimimum Cost:", min(cost), "The best monkey is", GL)
    print("The best route:", modified_arrays[GL])
    return True
