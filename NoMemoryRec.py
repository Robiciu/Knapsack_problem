def no_mem_rec(knapsack, max_weight, size):
    if max_weight == 0 or size == 0:
        return 0
    if knapsack[size-1][0] <= max_weight:
        return max(knapsack[size-1][1]+no_mem_rec(knapsack, max_weight-knapsack[size-1][0], size-1),
                   no_mem_rec(knapsack, max_weight, size-1))
    else:
        return no_mem_rec(knapsack, max_weight, size-1)
