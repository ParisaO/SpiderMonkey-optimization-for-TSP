# SpiderMonkey-optimization-for-TSP
Using the spider monkey optimization algorithm to solve the Traveling Salesman Problem. The method is modified to be useful for discrete optimization problems.

To run the code:
1- In the main.py file, change the name of "file_path" according to 1000_randomDistance.txt or 1000_randomDistance.txt according to your problem.
2- You can modify the parameters. Check the comments:
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
