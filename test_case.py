from Solution import find_max_min_numbers

# test case 1
matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

assert find_max_min_numbers(matrix_1) == 3

#test case 2
matrix_2 = [
    [1, 3, 5],
    [4, 2, 6],
    [7, 8, 9]
]

assert find_max_min_numbers(matrix_2) == 5

