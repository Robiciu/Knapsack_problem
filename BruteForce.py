from itertools import combinations


def brute_force(knapsack, max_weight, size):
    value = 0
    for i in range(1, size+1):
        for j in combinations(range(size), i):
                tmp_weight = 0
                tmp_value = 0
                for p in j:
                    tmp_weight += knapsack[p][0]
                    tmp_value += knapsack[p][1]
                if tmp_weight <= max_weight and tmp_value > value:
                    value = tmp_value
    return value


'''
def brute_force(knapsack, max_weight, size):
    comb = []
    value = 0
    optimal = []
    for i in range(1, size+1):
        for j in combinations(range(size), i):
            comb.append(j)
    for i in comb:
        tmp_weight = 0
        tmp_value = 0
        tmp_optimal = []
        for j in i:
            tmp_optimal.append(j)
            tmp_weight += knapsack[j][0]
            tmp_value += knapsack[j][1]
        if tmp_weight <= max_weight and tmp_value > value:
            optimal = tmp_optimal
    print(optimal)
'''