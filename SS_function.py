def SS_function(a1, a2):
    swaps = []
    j = 0

    while a1 != a2:
        for i in range(j, len(a1)):
            if i == a2.index(a1[i]):
                j += 1
            else:
                index2 = a1.index(a2[i])
                a1[i], a1[index2] = a1[index2], a1[i]
                swaps.append((i, index2))
    return swaps


def cost_calculator(route, distance_matrix):
    L = len(route)
    SUM = 0
    for i in range(L-1):
        SUM += distance_matrix[route[i]-1][route[i+1]-1]

    return SUM