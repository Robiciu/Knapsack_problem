def dynamic(knapsack, max_weight, size):
    matrix = []
    for i in range(size + 1):
        matrix.append([0] * (max_weight + 1))
    for i in range(1, size + 1):
        for j in range(1, max_weight + 1):
            if knapsack[i - 1][0] > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - knapsack[i - 1][0]] + knapsack[i - 1][1])
    return matrix[size][max_weight]


'''
def make_matrix(knapsack, max_weight, size):
    matrix = []
    for i in range(size + 1):
        matrix.append([0] * (max_weight + 1))
    for i in range(1, size + 1):
        for j in range(1, max_weight + 1):
            if knapsack[i - 1][0] > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - knapsack[i - 1][0]] + knapsack[i - 1][1])
    return matrix


def get_optimal(matrix, knapsack, max_weight, size):
    optimal = []
    i = size
    j = max_weight
    while i > 0:
        if matrix[i][j] > matrix[i-1][j]:
            optimal.append(i-1)
            i -= 1
            j -= knapsack[i-1][0]
        else:
            i -= 1
    return optimal[::-1]


def dynamic(knapsack, max_weight, size):
    matrix = make_matrix(knapsack, max_weight, size)
    optimal = get_optimal(matrix, knapsack, max_weight, size)
    print(optimal)
'''